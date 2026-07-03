import streamlit as st
import pickle
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
import gdown


movie_list = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies = movie_list['title'].values


try:
    API_KEY = st.secrets["TMDB_API_KEY"]
except (FileNotFoundError, KeyError):
    API_KEY = "00da7d605636a976d988bb9dd46d5889"

FALLBACK_POSTER = "https://placehold.co/300x450?text=No+Image"

def download_file(file_id, output):
    if not os.path.exists(output):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output, quiet=False)

download_file("1PH19sUma5yalGembsV_7mnbl6oyYZBtC", "tmdb_5000_movies.csv")
download_file("1AN4PDTUO_geZf622S-31cy5oWKjjDXw0", "tmdb_5000_credits.csv")
download_file("1RXy5qPEALEaQK3v7bczIRudzTL4v-_dO", "similarity.pkl")

def _session_with_retries():
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=0.5,         
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


SESSION = _session_with_retries()


@st.cache_data(show_spinner=False, ttl=60 * 60 * 24)  # cache for 24h
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    try:
        response = SESSION.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
        return FALLBACK_POSTER

    except requests.exceptions.RequestException as e:
        print(f"Error for movie {movie_id}: {e}")
        return FALLBACK_POSTER


def recommend(movie):
    movie_index = movie_list[movie_list['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movie_list.iloc[i[0]].movie_id
        recommended_movies.append(movie_list.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select Movie", movies)

if st.button("Recommend"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)

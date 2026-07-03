
# 🎬 Movie Recommendation System

A content-based movie recommendation system built using **Python**, **Streamlit**, and **Machine Learning**. This application recommends movies similar to the one selected by the user based on movie metadata from the TMDB 5000 Movies Dataset.

---

## 📌 Features

- Recommend movies based on content similarity
- Displays movie posters using the TMDB API
- Fast recommendations using a precomputed similarity matrix
- Simple and interactive Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Requests
- TMDB API

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md
├── tmdb_5000_movies.csv      (downloaded automatically)
├── tmdb_5000_credits.csv     (downloaded automatically)
└── similarity.pkl            (downloaded automatically)
```

---

## 🚀 How It Works

1. User selects a movie from the dropdown menu.
2. The application finds similar movies using cosine similarity.
3. Movie posters are fetched from the TMDB API.
4. The top recommended movies are displayed with their posters.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**, which contains movie metadata such as:

- Movie Title
- Genres
- Keywords
- Cast
- Crew
- Overview

The recommendation engine is built using **content-based filtering** with **cosine similarity**.

---

## ▶️ Running the Project Locally

### Clone the repository

```bash
git clone https://github.com/<your-username>/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

**Streamlit App:**  
Add your deployed Streamlit app link here.

Example:

```
https://movie-recommendation-system.streamlit.app
```

---

## 📷 Screenshots

Add screenshots of the application here after deployment.

Example:

- Home Page
- Recommended Movies
- Movie Posters

---

## 🔮 Future Improvements

- User authentication
- Search history
- Personalized recommendations
- Genre-based filtering
- Trending and popular movies
- Hybrid recommendation system

---

## 🙏 Acknowledgements

- TMDB (The Movie Database)
- Streamlit
- Scikit-learn
- Pandas

---

## 📧 Contact

**Ruturaj Chitale**

GitHub: https://github.com/<your-username>

LinkedIn: Add your LinkedIn profile here.

import requests

API_KEY = "00da7d605636a976d988bb9dd46d5889"

url = f"https://api.themoviedb.org/3/movie/7450?api_key={API_KEY}"

try:
    response = requests.get(url, timeout=10)
    print("Status:", response.status_code)
    print(response.json())
except Exception as e:
    print(type(e))
    print(e)
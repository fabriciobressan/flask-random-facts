#!/usr/bin/env python3
import requests

api_key = "76c467804bb0474fe96b4b38c3288eba"
search_url = "https://api.themoviedb.org/3/search/movie"

params = {
    'api_key': api_key,
    'query': 'Indiana Jones'
}

response = requests.get(search_url, params=params)

if response.status_code == 200:
    data = response.json()
    # Print the full response to see what data is available
    print(data)
else:
    print("Error:", response.status_code, response.text)
    
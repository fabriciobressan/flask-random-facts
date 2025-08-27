#!/usr/bin/env python3
import requests
# This is the URL of the API
api_url = "https://api.api-ninjas.com/v1/facts?"

# Replace this with your API key
api_key = "yaJNs0Tk1dWA7yzE9O2PgA==9jzwlAmWbUXTZ5sO"

# Send a request to the API
response = requests.get(
    api_url,
    headers={'X-Api-Key': api_key}
)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to a Python dictionary
    data = response.json()
    # Print the data
    print(data)
else:
    print("Error", response.status_code, response.text)
    
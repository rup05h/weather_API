# print('hello')
# http://api.weatherapi.com/v1/current.json?key=2617b16466c64de68ec21122240801&q=London

import requests

# Replace '<Your API Key>' with your actual Weather API key
api_key = '2617b16466c64de68ec21122240801'
location = "Melbourne"
url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

try:
    response = requests.get(url)
    data = response.json()

    # Print the response data
    print(data)

except requests.exceptions.RequestException as e:
    print(f"Error making the request: {e}")

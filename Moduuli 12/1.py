import requests

try:
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.get("value"))
    else:
        print(f"Error: Received status code {response.status_code}")
except requests.RequestException as e:
    print(f"An error occurred: {e}")

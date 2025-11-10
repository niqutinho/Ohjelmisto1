import requests

municipality = input("Enter municipality name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid=YOUR_API_KEY_HERE&units=metric"

response = requests.get(url)
weather_data = response.json()

if weather_data['cod'] == 200:
    description = weather_data['weather'][0]['description']
    temperature = weather_data['main']['temp']

    print(f"Weather: {description}")
    print(f"Temperature: {temperature} Celsius")
else:
    print(f"Error: {weather_data['message']}")
import requests

api_key = 'YOUR_API_KEY'
city = 'London'
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

try:
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f'Weather in {city}:')
    print(f'Description: {weather_description}')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind_speed} m/s')

except requests.exceptions.RequestException as error:
    print(f'Error fetching the weather data: {error}')
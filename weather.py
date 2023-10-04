import requests

# Replace YOUR_API_KEY with your actual API key
api_key = '19cf9579f86c42adb9344232233003'

# Replace CITY_NAME with the name of the city you want to get data for
city = 'Baltimore'
country_code = 'US'

# Make a request to OpenWeatherMap API to retrieve weather data
response = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric')

# Check if the request was successful
if response.status_code == 200:
    # Get temperature and humidity data from the response
    data = response.json()
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    # Print the temperature and humidity data
    print(f'The temperature in {city} is {temperature}°C.')
    print(f'The humidity in {city} is {humidity}%.')
else:
    print('Error retrieving weather data')
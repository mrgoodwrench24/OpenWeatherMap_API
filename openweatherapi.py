import requests

zip_code = input("Enter Zip/Postal Code\n")
country_code = "US"
api_key = 'a240c5f32cbaeae4252cc8746d06634b&'

zip_response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}%2CUS&appid={api_key}')

zip_data = zip_response.json()
zip_code = zip_data['zip']
city_name = zip_data['name']
latitude = zip_data['lat']
longitude = zip_data['lon']

weather_response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}=')

current_weather = weather_response.json()

current_conditions = current_weather['weather'][0]['description']
current_tempK = current_weather['main']['temp']
current_tempC = current_tempK - 273.15
current_tempf = (current_tempC * 9/5) + 32

tempf = float(current_tempf)

#print(response.status_code)  # Should print 200 if the request was successful
##print(response.json())       # Should print the response data in JSON format
print("You entered: " + zip_code)
print("Weather for " + city_name)
print(current_conditions)
print(f"\nCurrent temperature: {round(tempf)}")




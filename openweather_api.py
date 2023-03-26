import requests
country_code = 'US'
api_key = 'a240c5f32cbaeae4252cc8746d06634b&'

def get_city(zip_code):
    zip_response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}%2CUS&appid={api_key}')
    if zip_response.status_code ==200:
        zip_data = zip_response.json()
        zip_code = zip_data['zip']
        city_name = zip_data['name']
        latitude = zip_data['lat']
        longitude = zip_data['lon']
        print("You entered: " + zip_code)
        print("\nWeather for " + city_name)
        return latitude, longitude
    else:
        raise Exception("Invalid Zip Code")
                        #f"Error {zip_response.status_code}: {zip_response.text}

def get_current_conditions(latitude, longitude):
    weather_response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}=')
    if weather_response.status_code == 200:
        current_weather = weather_response.json()
        current_conditions = current_weather['weather'][0]['description']
        current_tempK = current_weather['main']['temp']
        current_tempC = current_tempK - 273.15
        current_tempf = (current_tempC * 9 / 5) + 32
        tempf = float(current_tempf)
        return current_conditions, tempf
    else:
        raise Exception(f"Error {weather_response.status_code}: {weather_response.text}")



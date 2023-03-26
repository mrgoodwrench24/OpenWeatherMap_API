import requests
from config import api_key
country_code = 'US'


def kelvin_to_fahrenheit(temp):
    #(K − 273.15) × 9/5 + 32 = °F.
    return ((temp - 273.15) * 9/5 + 32)

def get_city(zip_code):
    zip_response = requests.get(f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}%2CUS&appid={api_key}')
    if zip_response.status_code ==200:
        zip_data = zip_response.json()
        zip_code = zip_data['zip']
        city_name = zip_data['name']
        latitude = zip_data['lat']
        longitude = zip_data['lon']
        print("You entered: " + zip_code)
        city_dict ={'lat': latitude, 'long': longitude, 'city' : city_name}
        return city_dict
    else:
        raise Exception("Invalid Zip Code")
                        #f"Error {zip_response.status_code}: {zip_response.text}

def get_current_conditions(latitude, longitude):
    weather_response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}=')
    if weather_response.status_code == 200:
        current_weather = weather_response.json()
        current_conditions = current_weather['weather'][0]['description']

        current_temp = current_weather['main']['temp']
        current_tempf = float(kelvin_to_fahrenheit(current_temp))

        temp_feelK = current_weather['main']['feels_like']
        temp_feel = float(kelvin_to_fahrenheit(temp_feelK))

        today_lowK = current_weather['main']['temp_min']
        today_low = float(kelvin_to_fahrenheit(today_lowK))

        today_highK = current_weather['main']['temp_max']
        today_high = float(kelvin_to_fahrenheit(today_highK))

        conditions_dict = {'current_temp' : current_tempf, 'conditions' : current_conditions, 'current_feel' : temp_feel, 'low': today_low, 'high' : today_high}
        return conditions_dict
    else:
        raise Exception(f"Error {weather_response.status_code}: {weather_response.text}")



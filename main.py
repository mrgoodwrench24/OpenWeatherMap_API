from openweather_api import *

zip_code = input("Enter Zip/Postal Code\n")
city_dict = get_city(zip_code)
current_conditions_dict = get_current_conditions(city_dict['lat'], city_dict['long'])
print(f"\nCurrent Conditions for {city_dict['city']}\n")

print(current_conditions_dict['conditions'])
print(f"Current temperature: {round(current_conditions_dict['current_temp'])}F and feels like {round(current_conditions_dict['current_feel'])}F")
print(f"Today will have a low of {round(current_conditions_dict['low'])}F and a high of {round(current_conditions_dict['high'])}F.")
print(f"Current Wind Speed: {current_conditions_dict['wind_speed']} mph")




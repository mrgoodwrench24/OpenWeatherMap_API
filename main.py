from openweather_api import *

zip_code = input("Enter Zip/Postal Code\n")
latitude, longitude = get_city(zip_code)
current_conditions, temperature = get_current_conditions(latitude, longitude)

print(current_conditions)
print(f"Current temperature: {round(temperature)} F")




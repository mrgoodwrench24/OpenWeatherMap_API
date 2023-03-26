# OpenWeatherMap_API
README
This program utilizes the OpenWeatherMap API to retrieve current weather conditions for a given zip/postal code.

Installation

To run this program, first clone or download the repository to your local machine. You will also need to obtain an API key from OpenWeatherMap by signing up for an account on their website. Once you have your API key, create a file named config.py in the root directory of the project and set the variable api_key to your API key as a string.

This program requires the requests library to make API requests. If you do not already have it installed, you can install it by running the following command in your terminal/command prompt: pip install requests

Usage

To use this program, run main.py in your terminal/command prompt. You will be prompted to enter a zip/postal code for the location you want to retrieve weather data for. The program will then use the OpenWeatherMap API to retrieve the latitude and longitude coordinates of that location, and then retrieve the current weather conditions for those coordinates.

The program will display the current conditions, current temperature (in Fahrenheit), and the low and high temperatures for the current day (also in Fahrenheit) for the specified location.

Files

main.py: This is the main file that runs the program. It imports the openweather_api module and prompts the user to enter a zip/postal code for the location they want to retrieve weather data for. It then uses functions from the openweather_api module to retrieve and display weather data for that location.

openweather_api.py: This module contains functions for retrieving weather data from the OpenWeatherMap API. It includes functions to convert temperature units from Kelvin to Fahrenheit, retrieve the latitude and longitude coordinates for a given zip/postal code, and retrieve the current weather conditions for a given set of coordinates.

config.py: This file contains the API key for the OpenWeatherMap API. It should be included in the root directory of the project and should not be shared publicly.

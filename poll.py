#!/usr/bin/env python3
import pyowm
import os
import sys

def load_configuration():
    config = {}
    config['CITY_ID_SET'] = eval(os.environ.get('CITY_ID_SET', '()'))
    config['OPENWEATHERMAP_API_KEY'] = os.environ.get('OPENWEATHERMAP_API_KEY')
    return config


def print_error(message):
    sys.stderr.write(message)
    sys.stderr.flush()


def main():
    print("hello world")
    config = load_configuration()

    openweathermap_api_key = config['OPENWEATHERMAP_API_KEY']
    weather_api = pyowm.OWM(openweathermap_api_key)

    city_ids = config['CITY_ID_SET']

    if not city_ids:
        print("No City IDs were provided")

    for city_id in city_ids:
        observation = weather_api.weather_at_id(city_id)
        weather = observation.get_weather()
        print(weather.get_temperature('celsius'))

if __name__ == "__main__":
    main()

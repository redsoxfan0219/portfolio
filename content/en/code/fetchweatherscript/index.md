---
title: "Fetch Current Weather"
description: ""
lead: ""
date: 2022-10-20T23:34:43-04:00
lastmod: 2022-10-20T23:34:43-04:00
draft: false
images: []
menu:
  code:
    parent: ""
weight: 999
toc: true
---

I like knowing the weather as soon as I get up, and a simple Google search doesn't provide me all the weather details I want. So I wrote a Python script that gives me exactly what I want. Because I'll occasionally travel, I've set it up where I can enter the name of the city for which I want the weather details.

For more information on the API this script uses to retrieve the weather details, please see [this page](https://openweathermap.org/api). Keys for this API can be accessed after setting up an account. For security reasons, I've removed my API key details in the script below.

```python
import requests

def get_weather():

    def kelvin_to_fahrenheit(kelvin):
        fahrenheit = ((kelvin - 273.15) * (9/5) + 32)
        return fahrenheit

    def millibar_to_inchesHg(millibars):
        inHg = millibars / 33.864
        return inHg

    def pressure_rating(inHg):
        if inHg > 30.20:
            pressure = "High Pressure"
            return pressure
        elif 29.80 <= inHg < 30.20:
            pressure = "Medium Pressure"
            return pressure
        else:
            pressure = "Low Pressure"
            return pressure 
    
    def metersPerSecond_to_MPH(metersPerSecond):
        mph = metersPerSecond * metersPerSecond
        return mph

    api_key = 'fb5366fefa8f3e8dea18ae57bc024b7e'

    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    city = input('Enter city name: ')

    endpoint = f'{base_url}?q={city}&appid={api_key}'

    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp_kelvin = data['main']['temp']
        feels_like_kelvin = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_metric = data['wind']['speed']
        wind_speed = metersPerSecond_to_MPH(wind_metric)
        pressure_millibar = data['main']['pressure']
        pressure = millibar_to_inchesHg(pressure_millibar)
        pressure_rating = pressure_rating(pressure)
        temp = kelvin_to_fahrenheit(temp_kelvin)
        feels_like = kelvin_to_fahrenheit(feels_like_kelvin)

        print(f'Primary Weather: {main}')
        print(f'Description: {description}')
        print(f'Humidity: {humidity}%')
        print(f'Temperature: {temp:.1f}°F')
        print(f'Feels like: {feels_like:.1f}°F')
        print(f'Wind speed: {wind_speed:.1f} mph')
        print(f'Pressure: {pressure:.2f} inchesHg: {pressure_rating}')
        
    else: 
        error_code = response.status_code
        print(f'There was a {error_code} error')

if __name__ == '__main__':
    get_weather()

```
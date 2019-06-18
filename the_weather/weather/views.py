from django.shortcuts import render
import requests


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=fadf4949eac29a8cc732f222d6993339'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    return render(request, 'weather/index.html') #returns the index.html template

    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }

    return render(request, 'weather/index.html') #returns the index.html template

    return render(request, 'weather/index.html') #returns the index.html template
   
    context = {'weather' : weather}
    return render(request, 'weather/index.html', context) #returns the index.html template
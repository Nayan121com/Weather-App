
from django.shortcuts import render, HttpResponse
import os
import requests
from datetime import datetime
# Create your views here.
def index(request):
    return render(request, 'index.html')

def Earth(request):
    earth_api_key = 'b978dfd94fcf4e9b0a3599853102c76f'
    weather_dict = None
    if 'Earth_City' in request.GET :
        city_name = request.GET.get('Earth_City')
        Url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+earth_api_key
        earth_weather = requests.get(Url)
        earth_weather = earth_weather.json()
        weather_dict = {
        "city":city_name,
        "date" : datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
        "description": earth_weather["weather"][0]['description'],
        "temp": "{:.2f}".format(earth_weather['main']['temp'] - 273.15),
        "pressure":earth_weather['main']['pressure'],
        "humidity":earth_weather['main']['humidity'],
        "wind_speed":earth_weather["wind"]['speed']
        }      

    return render(request, 'Earth.html', {'earth_weather':weather_dict})

def Mars(request):
    mars_api_key = "KuBxJ1pqHk6t18l6XEzjjKlTPMmLVE0HeqdmMnzD"
    Url = "https://api.nasa.gov/insight_weather/?api_key="+mars_api_key+"&feedtype=json&ver=1.0"
    mars_weather = requests.get(Url)
    mars_weather = mars_weather.json()
    Present_sol = mars_weather['sol_keys']
    print(mars_weather)
    mars_dict = {
        "sol":Present_sol[6],
        "temp":Present_sol[6]['At']['av'],
        "Wind_s":Present_sol[6]['HWS']['av'],
        "pressure":Present_sol[6]['PRE']['av'],
        "date":datetime.todatetime(Present_sol[6]["First_UTC"]).strftime("%d / %m / %y, %H:%M:%S ")
    }
    return render(request, 'Mars.html', {"mars_weather":mars_dict})
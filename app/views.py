from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    city = request.GET.get("city", "bengaluru")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=17f2fbab506af2f13c75081cfec86b41&units=metric"
    api = requests.get(api_url).json()
    temp = api['main']['temp']
    country = api["sys"]["country"]
    city_name = api["name"]
    hum = api["main"]["humidity"]
    speed = api["wind"]["speed"]
    clouds = api["clouds"]["all"]
    icon = api["weather"][0]["icon"]
    weather = api["weather"][0]["main"]
    icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    return render(request, "index.html", {"temp":temp, "country":country, "city":city_name, "hum":hum, "speed":speed, "clouds":clouds, "icon":icon, "weather":weather})

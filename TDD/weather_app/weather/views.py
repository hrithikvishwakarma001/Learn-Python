from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.

# Weather data dictionary
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

class WeatherView(View):

    def get(self, request, city):
        city_data = weather_data.get(city)
        if city_data is None:
            return JsonResponse({'error': 'City not found'}, status=404)
        return JsonResponse(city_data)

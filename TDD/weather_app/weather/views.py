from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

weather_data = {
    "San Francisco": {"temperature": 14, "weather": "Cloudy"},
    "New York": {"temperature": 20, "weather": "Sunny"},
    "Los Angeles": {"temperature": 24, "weather": "Sunny"},
    "Seattle": {"temperature": 10, "weather": "Rainy"},
    "Austin": {"temperature": 32, "weather": "Hot"},
}

def get_weather_data(city):
    return weather_data.get(city)


@csrf_exempt
def get_weather(request, city):
    city_data = get_weather_data(city)
    if city_data is None:
        return JsonResponse({"error": "City not found"}, status=404)
    return JsonResponse(city_data, status=200)

@csrf_exempt
def create_weather(request):
    if request.method == "POST":
        data = json.loads(request.body)
        city = data.get("city")
        if city in weather_data:
            return JsonResponse({"error": "City already exists"}, status=400)
        weather_data[city] = {
            "temperature": data["temperature"],
            "weather": data["weather"],
        }
        return JsonResponse(data, status=201)

@csrf_exempt
def update_weather(request, city):
    if request.method == "PUT":
        data = json.loads(request.body)
        if city in weather_data:
            weather_data[city].update(data)
            return JsonResponse(data, status=200)
        return JsonResponse({"error": "City not found"}, status=404)

@csrf_exempt
def delete_weather(request, city):
    if request.method == "DELETE":
        if city in weather_data:
            del weather_data[city]
            return JsonResponse({"message": f"{city} Deleted successfully"}, status=204)
        return JsonResponse({"error": "City not found"}, status=404)
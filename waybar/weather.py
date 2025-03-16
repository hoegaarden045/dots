import requests
import json
import math

def get_weather_moscow():
    # Coordinates of Moscow
    latitude = 55.7558
    longitude = 37.6173
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    try:
        response = requests.get(url)

        data = response.json()
        temperature = data['current_weather']['temperature']
        weather_status = data['current_weather']['weathercode']

        temperature = math.ceil(temperature)
        weather_icons = {
            "clear": (" ", "Clear or mostly clear"),  # Code 0 and 1
            "partly_cloudy": ("⛅", "Partly cloudy"),     # Code 2
            "overcast": (" ", "Overcast"),       # Code 3
            "fog": (" ", "Fog"),                          # Code 45 and 48
            "drizzle": (" ", "Drizzle (light or moderate)"),  # Code 51, 53, 55
            "rain": (" ", "Rain (light, moderate, or heavy)"),  # Code 61, 63, 65
            "snow": (" ", "Snow (light, moderate, or heavy)"),     # Code 71, 73, 75
            "showers": (" ", "Showers (light or moderate)"),          # Code 80, 81, 82
            "thunderstorm": ("󰖓 ", "Thunderstorm")                        # Code 95, 96, 99
        }

        if weather_status in [0, 1]:
            weather_icon, weather_description = weather_icons["clear"]
        elif weather_status == 2:
            weather_icon, weather_description = weather_icons["partly_cloudy"]
        elif weather_status == 3:
            weather_icon, weather_description = weather_icons["overcast"]
        elif weather_status in [45, 48]:
            weather_icon, weather_description = weather_icons["fog"]
        elif weather_status in [51, 53, 55]:
            weather_icon, weather_description = weather_icons["drizzle"]
        elif weather_status in [61, 63, 65]:
            weather_icon, weather_description = weather_icons["rain"]
        elif weather_status in [71, 73, 75]:
            weather_icon, weather_description = weather_icons["snow"]
        elif weather_status in [80, 81, 82]:
            weather_icon, weather_description = weather_icons["showers"]
        elif weather_status in [95, 96, 99]:
            weather_icon, weather_description = weather_icons["thunderstorm"]
        else:
            weather_icon, weather_description = (" ", "Unknown weather condition")
        output = {
            "text" : f"Moscow {weather_icon} {temperature}°C",
        }
        print(json.dumps(output))
        #print(f"Moscow {weather_icon} {temperature}°C")
    except Exception:
        pass

get_weather_moscow()

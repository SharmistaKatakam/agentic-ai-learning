def weather_tool(city):
    weather_data = {
        "Hyderabad": "35°C Sunny",
        "Bangalore": "28°C Cloudy",
        "Mumbai": "32°C Rainy"
    }

    return weather_data.get(city, "Weather not available")

result = weather_tool("Hyderabad")

print(result)
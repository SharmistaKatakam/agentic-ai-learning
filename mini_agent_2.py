# Calculator Tool
def calculator_tool(a, b):
    return a + b


# File Tool
def file_tool(file_name):
    with open(file_name, "r") as file:
        return file.read()


# Weather Tool
def weather_tool(city):
    weather_data = {
        "Hyderabad": "35°C Sunny",
        "Bangalore": "28°C Cloudy",
        "Mumbai": "32°C Rainy"
    }

    return weather_data.get(city, "Weather not available")


question = input("Ask a question: ")

if "add" in question.lower():
    result = calculator_tool(100, 250)
    print("Agent selected: calculator_tool")
    print("Answer:", result)

elif "weather" in question.lower():
    result = weather_tool("Hyderabad")
    print("Agent selected: weather_tool")
    print("Answer:", result)

elif "read" in question.lower():
    result = file_tool("employees.txt")
    print("Agent selected: file_tool")
    print("Answer:")
    print(result)

else:
    print("I don't know which tool to use")
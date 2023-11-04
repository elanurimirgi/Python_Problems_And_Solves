#Homework1
import requests

API_KEY = '86c4f8ab88260f24b48988f4edbe5164'

def get_weather_info(city):
    base_url = "http://api.weatherstack.com/current"
    complete_url = f"{base_url}?access_key={API_KEY}&query={city}"

    response = requests.get(complete_url)
    
    data = response.json()

    if "current" in data:
        current_data = data["current"]
        temperature = current_data["temperature"]
        humidity = current_data["humidity"]
        weather_description = current_data["weather_descriptions"][0]

        print(f"Weather: {weather_description}")
        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or weather information could not be retrieved.")

if __name__ == "__main__":
    city = input("Enter the city for which you want to get weather information: ")
    get_weather_info(city)

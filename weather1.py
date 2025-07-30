import requests

API_KEY = "916988b9cee240c9bb1163450253007"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city_name):
    url = f"{BASE_URL}?key={API_KEY}&q={city_name}&aqi=no"
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        
        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]

        print("\n Weather Report")
        print(f"City       : {location}, {region}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition  : {condition}")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} km/h")

    except requests.exceptions.HTTPError as http_err:
        print(f" HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f" Error: {err}")
    except KeyError:
        print(" City not found or unexpected API response.")

def main():
    print("Welcome to the Weather App!")
    city = input("Enter city name: ").strip()
    
    if city:
        get_weather(city)
    else:
        print(" Please enter a valid city name.")


main()

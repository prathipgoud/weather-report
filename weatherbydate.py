import requests

API_KEY = "916988b9cee240c9bb1163450253007"
BASE_URL = "http://api.weatherapi.com/v1/history.json"

def get_historical_weather(city_name, date):
    """Fetch and display historical weather data for a city and date."""
    url = f"{BASE_URL}?key={API_KEY}&q={city_name}&dt={date}&aqi=no"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]

        print("\nWeather Report")
        print(f"Date       : {date}")
        print(f"City       : {location['name']}, {location['region']}, {location['country']}")
        print(f"Temperature: {temperature}°C")
        print(f"Condition  : {condition}")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} km/h")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except (KeyError, IndexError):
        print("City not found, date out of range, or unexpected API response.")

def main():
    print("Welcome to the Historical Weather App!")
    city = input("Enter city name: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    if city and date:
        get_historical_weather(city, date)
    else:
        print("Please enter both a valid city name and date.")


main()

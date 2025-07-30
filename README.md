Weather CLI Application
-----------------------

Description:
This is a command-line weather application built in Python. It allows you to check current weather information for any city using WeatherAPI.

Requirements:
- Python 3.x
- Internet connection
- requests module (install using pip if not available)

How to Run:
1. Open terminal in project folder.
2. Run the script using:
   python weather_app.py
3. Enter the city name when prompted.

API Used:
- WeatherAPI (https://www.weatherapi.com/)
- API Key: 916988b9cee240c9bb1163450253007

Output:
- City Name
- Region and Country
- Temperature in Celsius
- Weather Condition (e.g., Clear, Mist)
- Humidity and Wind Speed

Errors Handled:
- Invalid city
- API errors (HTTP errors, network issues)
- Empty input

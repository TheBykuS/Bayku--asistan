# weather.py
import requests

def get_weather(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"

    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            city_name = data["name"]
            weather_info = f"{city_name} için hava durumu: {temp} derece ve {weather}."
            return weather_info
        else:
            return "Hava durumu bilgisi alınamadı."
    except Exception as e:
        return f"Bir hata oluştu: {e}"

import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY_HERE"  # ← Replace this with your WeatherAPI key!
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    if "location" in data:
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        result_label.config(
            text=(
                f"📍 {location}, {country}\n"
                f"🌡️ Temp: {temp}°C\n"
                f"🌥️ Condition: {condition}"
            )
        )
    else:
        result_label.config(text="❌ City not found or API issue.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
result_label.pack(pady=20)

root.mainloop()


# or if no needed gui stepup

# Comment out or remove this part if you don't want GUI:
# root = tk.Tk()
# ...

def get_weather_console(city):
    api_key = "YOUR_API_KEY_HERE"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()
    if "location" in data:
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"📍 {location}, {country}")
        print(f"🌡️ Temp: {temp}°C")
        print(f"🌥️ Condition: {condition}")
    else:
        print("❌ City not found or API issue.")



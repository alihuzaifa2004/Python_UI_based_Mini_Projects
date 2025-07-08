import tkinter as tk
from tkinter import messagebox
import requests

# Replace with your WeatherAPI key
API_KEY = 'Enter your Api'

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        weather_data = response.json()

        if 'error' in weather_data:
            messagebox.showerror("Error", weather_data['error'].get('message', 'City not found'))
            return

        temp = weather_data['current']['temp_c']
        condition = weather_data['current']['condition']['text']
        humidity = weather_data['current']['humidity']
        wind_speed = weather_data['current']['wind_kph']

        result_label.config(
            text=f"City: {city}\nTemperature: {temp}°C\nCondition: {condition}\n"
                 f"Humidity: {humidity}%\nWind Speed: {wind_speed} km/h"
        )

    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data.")

# Create the main window
app = tk.Tk()
app.title("Weather App (WeatherAPI)")
app.geometry("400x350")
app.resizable(False, False)

# Heading
heading_label = tk.Label(app, text="Weather App", font=("Arial", 20, "bold"))
heading_label.pack(pady=10)

# City Entry
city_entry = tk.Entry(app, font=("Arial", 14))
city_entry.pack(pady=10)

# Search Button
search_button = tk.Button(app, text="Get Weather", font=("Arial", 14), bg="blue", fg="white", command=get_weather)
search_button.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14), justify="left")
result_label.pack(pady=20)

# Run the app
app.mainloop()

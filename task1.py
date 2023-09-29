import tkinter as tk
import requests
from tkinter import messagebox

# Replace 'YOUR_API_KEY' with your  OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name):
    try:
        params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] == 200:
            temperature = data["main"]["temp"]
            weather_description = data["weather"][0]["description"]
            weather_info_label.config(
                text=f'Temperature: {temperature}°C\nDescription: {weather_description}')
        else:
            messagebox.showerror('Error', 'City not found')
    except Exception as e:
        messagebox.showerror('Error', str(e))

def get_weather():
    city_name = city_entry.get()
    if city_name:
        get_weather_data(city_name)
    else:
        messagebox.showerror('Error', 'Please enter a city name')

# Creating the main window
app = tk.Tk()
app.title('Weather App')

# Creating  and configure widgets
city_label = tk.Label(app, text='Enter city name:')
city_entry = tk.Entry(app)
get_weather_button = tk.Button(app, text='Get Weather', command=get_weather)
weather_info_label = tk.Label(app, text='')

#  All Pack widgets
city_label.pack()
city_entry.pack()
get_weather_button.pack()
weather_info_label.pack()

# Start the main loop
app.mainloop()
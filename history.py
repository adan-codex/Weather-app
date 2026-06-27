import csv
from tkinter import *


def save_history(city, temp, condition, time):

    with open("weather_history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            f"City: {city}",
            f"Temp: {temp}°C",
            f"Condition: {condition}",
            f"Time: {time}"
        ])


def show_history():

    window = Toplevel()
    window.title("Weather History")
    window.geometry("600x400")

    Label(
        window,
        text="Search History",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    text_area = Text(window, width=70, height=20)
    text_area.pack(pady=10)

    try:
        with open("weather_history.csv", "r") as file:
            text_area.insert(END, file.read())

    except FileNotFoundError:
        text_area.insert(END, "No history available.")
from tkinter import *


def show_about():

    window = Toplevel()
    window.title("About Project")
    window.geometry("400x250")

    Label(
        window,
        text="Weather App",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    Label(
        window,
        text="Built using Python Tkinter",
        font=("Arial", 12)
    ).pack()

    Label(
        window,
        text="\nTeam Members:",
        font=("Arial", 12, "bold")
    ).pack()

    Label(
        window,
        text="""
Adan Sarfraz
Ammar Arif
Ali Asghar
""",
        font=("Arial", 11)
    ).pack()

    Label(
        window,
        text="\nWeather Data: WeatherAPI",
        font=("Arial", 10)
    ).pack()
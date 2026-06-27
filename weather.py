from tkinter import *
import tkinter  as tk
from tkinter import ttk,messagebox
from datetime import datetime
from datetime import datetime
import requests
from history import save_history, show_history


root = Tk()
root.title("Weather App")
root.geometry("900x500")


def getWeather():
    city = textfeild.get()
    name.config(text="CURRENT WEATHER")
    
    # weather api
    api = "https://api.weatherapi.com/v1/current.json?key=fd91d7c85774464bb59140303260106&q="+city+"&aqi=no"
    try:
      response = requests.get(api)
      json_data = response.json()
      if "error" in json_data:
        messagebox.showerror("Error", json_data["error"]["message"])
        return
    except Exception as e:
       messagebox.showerror("Error", str(e))
       return
    # json_data = requests.get(api).json()
    localtime = json_data["location"]["localtime"]
    time_only = datetime.strptime(localtime, "%Y-%m-%d %H:%M").strftime("%I:%M %p")
    clock.config(text=time_only)
    
    wind = float(json_data["current"]["wind_mph"])
    temp = float(json_data["current"]["feelslike_c"])
    humidity = float(json_data["current"]["humidity"])
    pressure = float(json_data["current"]["pressure_in"])
    condition = json_data["current"]["condition"]["text"]
    save_history(
    city,
    temp,
    condition,
    time_only
    )
    
    rain = json_data["current"]["chance_of_rain"]

    
    
    t.config(text=f"{temp}°")
    c.config(text=f"{condition} | FEELS LIKE {temp}°")
    w.config(text=f"{wind} mph")
    h.config(text=f"{humidity}%")
    p.config(text=f"{pressure} in")
    r.config(text = (rain, "%"))

# search box
search_image = PhotoImage(file="Search bar.png")
myimage = Label(image=search_image,)
myimage.place(x=20, y=20)

textfeild = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfeild.place(x=50, y=40)
textfeild.focus()

# search_icon

search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image = search_icon, borderwidth=0, cursor="hand2",bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# logo

Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=150,y=100)

# bottom image

frame_image = PhotoImage(file="detail box.png")
frame_myimage = Label(image=frame_image)
frame_myimage.pack(padx=5, pady= 5, side= BOTTOM)

# time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Halvetica", 20))
clock.place(x=30, y=130)

# label 

label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="CHANCE OF RAIN", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label3.place(x=410, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70 , "bold"), fg="#ee666d")
t.place(x=400, y=150)
c=Label(font=("arial",15 , "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 17, "bold"), bg="#1ab5ef")
w.place(x=120, y= 430)

h = Label(text="...", font=("arial", 17, "bold"), bg="#1ab5ef")
h.place(x=250, y= 430)

r = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
r.place(x=430, y= 430)

p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=650, y= 430)
history_button = Button(
    root,
    text="View History",
    font=("Arial", 10, "bold"),
    command=show_history
)

history_button.place(x=760, y=60)

root.mainloop()

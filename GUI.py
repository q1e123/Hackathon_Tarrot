from tkinter import *
from PIL import Image, ImageTk
import weather

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   

def output():
    input = entry.get()
    temp, umid, vant = weather.predict(input)
    

root = Tk()
root.title("Weather prediction")
root.geometry("600x600")
root.configure(background="black")
text = Label(root, text = "Welcome to Tarot for weather, my friend!", bg = "black", fg = "white")
text.config(font=("Chiller", 20))
textPredict = Label(root, text = "Enter your date to be predicted: ", bg = "black", fg = "white", relief = "solid")
text.pack()
Space()
textPredict.pack()
entry = Entry (root) 
entry.pack()
Space()


button = Button(root, text = "Get Predicion", command = output, state = ACTIVE)
button.pack()
Space()
temp = Label(root, text = "Temperature: ")
temp.pack()
hum = Label(root, text = "Humidity: ")
hum.pack()
press = Label(root, text = "Pressure: ")
press.pack()
root.mainloop()
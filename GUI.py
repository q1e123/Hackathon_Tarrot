from tkinter import *
from PIL import Image, ImageTk

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   
    
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
button = Button(root, text = "Get tarot card")
button.pack()

root.mainloop()
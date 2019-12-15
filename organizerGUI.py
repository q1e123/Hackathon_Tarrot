from tkinter import *
from PIL import Image, ImageTk
import weather

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   

class User_Data:
    def __init__(self, pwd, temp, umd, wind,mail):
        self.pwd = pwd
        self.temp = temp
        self.umd = umd
        self.wind = wind 
        self.mail = mail

def get_dict():
    users = []
    db = open('userDB','r')
    lines = db.readlines()
    for user in lines:
        data = user.split(';')
        users[data[0]] = User_Data(data[1],data[2],data[3],data[4],data[5])
    return users

dic = get_dict()

def output():
    input = entry.get()
    tempr, umid, vant = weather.predict(input)
    db = open('outputDB','a+')        
    temp.configure(text = "Temperature: " + str(tempr))
    hum.configure(text = "Humidity: "+ str(umid))
    press.configure(text = "Wind: "+str(vant))
    stringMare = ""
    for users in dic:
        temp0,temp1 = users.temp.split('-')
        hum0, hum1 = users.umd.split('-')
        wind0, wind1 = users.wind.split('-')
        if temp0<=tempr<=temp1 and hum0<=umid<=hum1 and wind0<=vant<=wind1:
            stringMare+=user+user.mail
    people.config(text = "People expected to come at event:"+stringMare)

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
button = Button(root, text = "Get Prediction", command = output, state = ACTIVE)
button.pack()
Space()
temp = Label(root, text = "Temperature: ", bg = "black", fg = "white")
temp.pack()
hum = Label(root, text = "Humidity: ", bg = "black", fg = "white")
hum.pack()
press = Label(root, text = "Pressure: ", bg = "black", fg = "white")
press.pack()
people = Label(root, text = "People expected to come at event:", bg = "black", fg = "white")
people.pack()
root.mainloop()
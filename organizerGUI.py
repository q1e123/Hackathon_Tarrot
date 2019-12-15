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
    dic = {}
    db = open('userDB','r')
    lines = db.readlines()
    for user in lines:
        data = user.split(';')
        dic[data[0]] = User_Data(data[1],data[2],data[3],data[4],data[5])
    return dic

def get_key(val): 
    for key, value in dic.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def output():
    input = entry.get()
    dic = get_dict()
    tempr, umid, vant = weather.predict(input)
    db = open('outputDB','a+')        
    temp.configure(text = "Temperature: " + str(tempr))
    hum.configure(text = "Humidity: "+ str(umid))
    press.configure(text = "Wind: "+str(vant))
    stringMare = ""
    for users in dic.values():
        temp0,temp1 = map(float,users.temp.split('-'))
        hum0, hum1 = map(float,users.umd.split('-'))
        wind0, wind1 = map(float,users.wind.split('-'))
        if temp0<=tempr<=temp1 and hum0<=umid<=hum1 and wind0<=vant<=wind1:
            stringMare+=get_key(users)+' '+users.mail
    people.config(text = "People expected to come at event:\n"+stringMare)

def get_org_win():
    global root
    root = Tk()
    root.title("Weather prediction")
    root.geometry("600x600")
    root.configure(background="black")
    global text
    text = Label(root, text = "Weather predicter", bg = "black", fg = "white")
    text.config(font=("Chiller", 20))
    global textPredict
    textPredict = Label(root, text = "Enter your date to be predicted: ", bg = "black", fg = "white", relief = "solid")
    text.pack()
    Space()
    textPredict.pack()
    global entry
    entry = Entry (root) 
    entry.pack()
    Space()
    global button
    button = Button(root, text = "Get Prediction", command = output, state = ACTIVE)
    button.pack()
    Space()
    global temp
    temp = Label(root, text = "Temperature: ", bg = "black", fg = "white")
    temp.pack()
    global hum
    hum = Label(root, text = "Humidity: ", bg = "black", fg = "white")
    hum.pack()
    global press
    press = Label(root, text = "Pressure: ", bg = "black", fg = "white")
    press.pack()
    global people
    people = Label(root, text = "People expected to come at event:", bg = "black", fg = "white")
    people.pack()
    root.mainloop()

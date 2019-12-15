from tkinter import *
import hashlib
import subprocess
import loginGUI

class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password

def get_users():
    users = []
    db = open('userDB','r')
    lines = db.readlines()
    for user in lines:
        data = user.split(';')
        users.append(data[0])

    return users

userList = get_users()

def put_data():
    db = open("userDB",'a+')
    usr = entryUsername.get()
    if usr in userList:
        textUsername.config(fg = "red")
        return
    pwd = hashlib.sha256(entryPassword.get().encode('utf-8')).hexdigest()
    temp = entryTemp.get()
    umid = entryUmid.get()
    wind = entryWind.get()
    mail = entryMail.get()
    db.write(usr+';'+pwd+';'+temp+';'+umid+';'+wind+';'+mail+ '\n')
    Tk.quit()
    loginGUI.get_login_win()

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()

def get_register_win():
    global root
    root = Tk()
    root.title("Register Page")
    root.geometry("600x600")
    root.configure(background="black")
    global text
    text = Label(root, text = " Create an account", bg = "black", fg = "white")
    text.config(font=("Chiller", 20))
    text.pack()
    Space()
    global textUsername
    textUsername = Label(root, text = "Enter username: ", bg = "black", fg = "white")
    textUsername.pack()
    global entryUsername
    entryUsername = Entry (root) 
    entryUsername.pack()
    Space()
    global textPassword
    textPassword = Label(root, text = "Enter password: ", bg = "black", fg = "white")
    textPassword.pack()
    global entryPassword
    entryPassword = Entry(root) 
    bullet = "\u2022"
    entryPassword.config(show=bullet)
    entryPassword.pack()
    Space()
    global textTemp
    textTemp = Label(root, text = "Enter temperature: ", bg = "black", fg = "white")
    textTemp.pack()
    global entryTemp
    entryTemp = Entry(root) 
    entryTemp.pack()
    Space()
    global textUmid
    textUmid = Label(root, text = "Enter humitidy: ", bg = "black", fg = "white")
    textUmid.pack()
    global entryUmid
    entryUmid = Entry(root) 
    entryUmid.pack()
    Space()
    global textWind
    textWind = Label(root, text = "Enter wind: ", bg = "black", fg = "white")
    textWind.pack()
    global entryWind
    entryWind = Entry(root) 
    entryWind.pack()
    Space()
    global textMail
    textMail = Label(root, text = "Enter mail: ", bg = "black", fg = "white")
    textMail.pack()
    global entryMail
    entryMail = Entry(root) 
    entryMail.pack()
    
    Space()
    global buttonLogin
    buttonLogin = Button(root, text = "REGISTER", command = put_data, state = ACTIVE)
    buttonLogin.pack()
    root.mainloop()

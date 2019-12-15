from tkinter import *
from PIL import Image, ImageTk


def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   

def input():
    f = open("userDB", "w")
    input = entryUsername.get()
    f.write(input + "; ")
    input = entryPassword.get()
    f.write(input + "\n")

class User_Data:
    def __init__(self, pwd, temp, umd, wind,mail):
        self.pwd = pwd
        self.temp = temp
        self.umd = umd
        self.wind = wind 
        self.mail = mail

def get_dict():
    users = {}
    db = open('userDB','r')
    lines = db.readlines()
    for user in lines:
        data = user.split(';')
        users[data[0]] = User_Data(data[1],data[2],data[3],data[4],data[5])

    return users

dic = get_dict()

def login():
    usr = entryUsername.get()
    pwd = entryPassword.get()

    if dic[usr].pwd == pwd:
        print('LOGGED')
    else:
        print('WRONG')

root = Tk()
root.title("Log In Page")
root.geometry("600x600")
root.configure(background="black")
text = Label(root, text = " User Login", bg = "black", fg = "white")
text.config(font=("Chiller", 20))
text.pack()
Space()
textUsername = Label(root, text = "Enter username: ", bg = "black", fg = "white")
textUsername.pack()
entryUsername = Entry (root) 
entryUsername.pack()
Space()
textPassword = Label(root, text = "Enter password: ", bg = "black", fg = "white")
textPassword.pack()
entryPassword = Entry (root) 
bullet = "\u2022"
entryPassword.config(show=bullet)
entryPassword.pack()
Space()
buttonLogin = Button(root, text = "LOG IN", command = login, state = ACTIVE)
buttonLogin.pack()
root.mainloop()
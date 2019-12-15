from tkinter import *
from PIL import Image, ImageTk
import hashlib
import fileinput

import user_reco
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
    users = {}
    db = open('userDB','r')
    lines = db.readlines()
    for user in lines:
        data = user.split(';')
        users[data[0]] = User_Data(data[1],data[2],data[3],data[4],data[5])

    db.close()
    return users

dic = get_dict()

def login():
    usr = entryUsername.get()
    pwd = hashlib.sha256(entryPassword.get().encode('utf-8')).hexdigest()

    if dic[usr].pwd == pwd:
        print('LOGGED')
        user_screen(usr)
    else:
        print('WRONG')

def utos(usr):
    return usr+';'+dic[usr].pwd+';'+dic[usr].temp+';'+dic[usr].umd+';'+dic[usr].wind+';'+dic[usr].mail

def update(usr,widgets):
    old = utos(usr)
    new = usr+';'+dic[usr].pwd+';'+widgets[0].get()+';'+widgets[1].get()+';'+widgets[2].get()+';'+dic[usr].mail
    
    with fileinput.FileInput("userDB", inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(old, new), end='')
    widgets[3].config(background='#daffc2')

  

def user_screen(usr):
    text.config(text='Welcome ' + usr)

    textUsername.pack_forget()
    textPassword.pack_forget()
    entryPassword.pack_forget()
    entryUsername.pack_forget()
    buttonLogin.pack_forget()
    facial.pack_forget()
    widgets = []
    entrytemp = Entry (root) 
    entrytemp.insert(0, dic[usr].temp)    
    entrytemp.pack()
    widgets.append(entrytemp)
    Space()
    entryumd = Entry (root) 
    entryumd.insert(0, dic[usr].umd)    
    entryumd.pack()
    widgets.append(entryumd)
    Space()
    entrywind = Entry (root) 
    entrywind.insert(0, dic[usr].wind)    
    entrywind.pack()
    widgets.append(entrywind)
    Space()
    updateLogin = Button(root, text = "Update", command = lambda: update(usr,widgets), state = ACTIVE)
    updateLogin.pack()
    widgets.append(updateLogin)


def facial_recon_login(button):
    possible = user_reco.get_face()
    if possible in dic:
        user_screen(possible)
    else:
        button[0].config(background='#ff8585')

def get_login_win():
    global root 
    root = Tk()
    root.title("Log In Page")
    root.geometry("600x600")
    root.configure(background="black")
    global text
    text = Label(root, text = " User Login", bg = "black", fg = "white")
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
    entryPassword = Entry (root) 
    bullet = "\u2022"
    entryPassword.config(show=bullet)
    entryPassword.pack()
    Space()
    global buttonLogin
    buttonLogin = Button(root, text = "LOG IN", command = login, state = ACTIVE)
    buttonLogin.pack()

    Space()
    fac = []
    global facial
    facial = Button(root, text = "Facial log in", command = lambda: facial_recon_login(fac), state = ACTIVE)
    facial.pack()
    fac.append(facial)
    root.mainloop()
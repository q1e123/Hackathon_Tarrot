from tkinter import *
from tkinter.messagebox import showinfo

class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password


def put_data():
    db = open("userDB",'a+')
    usr = entryUsername.get()
    pwd = entryPassword.get()
    temp = entryTemp.get()
    umid = entryUmid.get()
    wind = entryWind.get()
    mail = entryMail.get()

    db.write(usr+';'+pwd+';'+temp+';'+umid+';'+wind+';'+mail+ '\n')


def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   

root = Tk()
root.title("Register Page")
root.geometry("600x600")
root.configure(background="black")
text = Label(root, text = " Create an account", bg = "black", fg = "white")
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
entryPassword = Entry(root) 
bullet = "\u2022"
entryPassword.config(show=bullet)
entryPassword.pack()
Space()
textTemp = Label(root, text = "Enter temperature: ", bg = "black", fg = "white")
textTemp.pack()
entryTemp = Entry(root) 
entryTemp.pack()
Space()
textUmid = Label(root, text = "Enter humitidy: ", bg = "black", fg = "white")
textUmid.pack()
entryUmid = Entry(root) 
entryUmid.pack()
Space()
textWind = Label(root, text = "Enter wind: ", bg = "black", fg = "white")
textWind.pack()
entryWind = Entry(root) 
entryWind.pack()
Space()
textMail = Label(root, text = "Enter mail: ", bg = "black", fg = "white")
textMail.pack()
entryMail = Entry(root) 
entryMail.pack()


Space()
buttonLogin = Button(root, text = "REGISTER", command = put_data, state = ACTIVE)
buttonLogin.pack()


root.mainloop()
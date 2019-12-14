from tkinter import *
from tkinter.messagebox import showinfo

class User():

    def __init__(self, username, password):
        self.username = username
        self.password = password

def login_btn_clicked(user):
    with open('userDB', 'a+') as f:
        reader = f.readline().split(';')
        my_dict = {k:v for k,v in reader}
    user1 = user.username
    password1 = user.password
    if (my_dict[user1]) == (password1):
        welcome1 = ("Welcome", user1)
        

    else:
        showinfo(title="Error", message="Account already existing")

def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()   

def input():
    f = open('userDB', 'a+')
    password = entryUsername.get()
    username = entryPassword.get()
    user = User(username, password)
    login_btn_clicked(user)
    f.write(input + "; ")
    f.write(input + "\n")

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
buttonLogin = Button(root, text = "REGISTER", command = input, state = ACTIVE)
buttonLogin.pack()


root.mainloop()
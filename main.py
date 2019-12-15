from tkinter import *
import registerGUI
import loginGUI
import organizerGUI
import user_facial_register
def Space():
    br = Label(root, text = "", bg = "black")
    br.pack()

def get_main_win():
    global root
    root = Tk()
    root.title("Main Page")
    root.geometry("300x300")
    root.configure(background="black")
    global text
    text = Label(root, text = "Main page", bg = "black", fg = "white")
    text.config(font=("Chiller", 20))
    text.pack()
    Space()
    global buttonorg
    buttonorg= Button(root, text = "Organizer", command = organizerGUI.get_org_win, state = ACTIVE)
    buttonorg.pack()
    Space()
    root.configure(background="black")
    global buttonreg
    buttonreg = Button(root, text = "New user", command = registerGUI.get_register_win, state = ACTIVE)
    buttonreg.pack()
    Space()
    root.configure(background="black")
    global buttonlog
    buttonlog = Button(root, text = "Existing user", command = loginGUI.get_login_win, state = ACTIVE)
    buttonlog.pack()
    Space()

    global buttonfacreg
    buttonfacreg= Button(root, text = "Generate face set", command = user_facial_register.get_facreg_win, state = ACTIVE)
    buttonfacreg.pack()
    Space()

    root.mainloop()

get_main_win()
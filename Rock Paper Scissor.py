from tkinter import *
from random import choice
root = Tk()
root.geometry("400x400")
root.title("ROCK PAPER SCISSOR")

def rock():
    userChoice["text"]= "User choice is: Rock"
    com_list = ["Rock","Paper","Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"
    rock_btn["stat"] = "disabled"
    paper_btn["stat"] = "disabled"
    scissor_btn["stat"] = "disabled"
    if com_list_choice == "Rock":
        msg["text"] = "It is Draw"
    if com_list_choice == "Paper":
        msg["text"] = "Computer wins!!"
    if com_list_choice == "Scissor":
        msg["text"] = "User wins!!"
def paper():
    userChoice["text"] = "User choice is: Paper"
    com_list = ["Rock","Paper","Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"
    rock_btn["stat"] = "disabled"
    paper_btn["stat"] = "disabled"
    scissor_btn["stat"] = "disabled"
    if com_list_choice == "Rock":
        msg["text"] = "User wins!!"
    if com_list_choice == "Paper":
        msg["text"] = "It is Draw"
    if com_list_choice == "Scissor":
        msg["text"] = "Computer wins!!"
def scissor():
    userChoice["text"] = "User choice is: Scissor"
    com_list = ["Rock","Paper","Scissor"]
    com_list_choice = choice(com_list)
    comChoice["text"] = f"Computer choice is: {com_list_choice}"
    rock_btn["stat"] = "disabled"
    paper_btn["stat"] = "disabled"
    scissor_btn["stat"] = "disabled"
    if com_list_choice == "Rock":
        msg["text"] = "Computer wins!!"
    if com_list_choice == "Paper":
        msg["text"] = "User wins!!"
    if com_list_choice == "Scissor":
        msg["text"] = "It is Draw"

def active():
    rock_btn["stat"] = "normal"
    paper_btn["stat"] = "normal"
    scissor_btn["stat"] = "normal"
    msg["text"] = ""
    comChoice["text"] = ""
    userChoice["text"] = ""

userChoice=Label(root,text="")
userChoice.pack()

rock_btn = Button(root,text="Rock", bg="violet",fg="black",font=("bold"), width=50,height=2,command=rock)
paper_btn = Button(root,text="Paper", bg="violet",fg="black", font=("bold"), width=50,height=2,command=paper)
scissor_btn = Button(root,text="Scissor",  bg="violet",fg="black",font=("bold"), width=50,height=2,command=scissor)
active_btn = Button(root,text="Play Again", bg="white",fg="black",font=("bold"), width=50,height=2,command=active)
rock_btn.pack()
paper_btn.pack()
scissor_btn.pack()


comChoice = Label(root,text="")
comChoice.pack()
msg = Label(root,text="",font=("Helvetica",17,"bold"))
msg.pack()

active_btn.pack()


root.mainloop()

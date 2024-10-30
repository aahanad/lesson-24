from tkinter import*
import tkinter.messagebox
import random
screen=Tk()
screen.geometry("680x600")
screen.title("guess the number")
screen.config(background="MediumPurple1")
number=random.randint(1,20)
def message():
    my_name=put.get()
    tkinter.messagebox.showinfo(f"Hi {my_name}","Im thinking of  number from 1-20 can you guess what it is?")
def submit():
    global number
    user=int(put2.get())
    if user<number:
        tkinter.messagebox.showinfo(f"too low!! :(","pick another number")
    elif user>number:
        tkinter.messagebox.showinfo(f"too high!! :(","pick another number")
    elif user==number:
        tkinter.messagebox.showinfo(f"Thats the right number!!","great job!!!:-)☺🙌")
title=Label(screen,text="Welcome to the number guess game!🔮",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
title.grid(row=1,column=1,padx=140,pady=50)
name=Label(screen,text="What is your name?",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
name.grid(row=2,column=1,padx=0,pady=50)
put=Entry(screen)
put.grid(row=2,column=2,padx=0,pady=50)
ok=Button(screen,text="ok",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"),command=message)
ok.grid(row=2,column=3,padx=15,pady=50)
guess=Label(screen,text="Take a guess:",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
guess.grid(row=3,column=1,padx=0,pady=70)
put2=Entry(screen)
put2.grid(row=3,column=2,padx=0,pady=50)
submit=Button(screen,text="Submit",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"),command=submit)
submit.grid(row=3,column=3,padx=15,pady=70)
screen.mainloop()
#Complete your distance calculator, you can also try working on some other quiz with 2 random numbers like guessing the addition or subtraction
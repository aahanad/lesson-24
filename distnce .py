from tkinter import*
screen=Tk()
screen.geometry("680x600")
screen.title("distance calc")
screen.config(background="MediumPurple1")
def get_distance():
    speed=int(put1.get())
    time=int(put.get())
    real=str(((speed)*(time)))
    aswer.config(text=real)
title=Label(screen,text="distance calculator",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
title.grid(row=1,column=1,padx=140,pady=50)
senter=Label(screen,text="speed=",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
senter.grid(row=2,column=1,padx=0,pady=50)
put1=Entry(screen)
put1.grid(row=2,column=2,padx=0,pady=50)
denter=Label(screen,text="time=",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"))
denter.grid(row=3,column=1,padx=0,pady=70)
put=Entry(screen)
put.grid(row=3,column=2,padx=0,pady=50)
calc=Button(screen,text="calculate distance",bg="CadetBlue1",fg="MediumPurple1",font=("Lola",15,"bold"),command=get_distance)
calc.grid(row=4,column=1,padx=90,pady=50)
aswer=Label(screen,bg="MediumPurple1",fg="CadetBlue1",font=("Lola",15,"bold"))
aswer.grid(row=5,column=2,padx=100,pady=50)
screen.mainloop()
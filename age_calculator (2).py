from tkinter import *

game=Tk()


import datetime    

def message(event):
    
    E=datetime.datetime.now()
    month=int(E3.get())
    M=int(E.month)==
    W3=int()
    MM=int()
    M=int(E.month)
    y=""


    if month>M:
    
        W3=int(month-M)
        MM=int(12-W3)
        M=str(MM)
        L4.configure(text= M  + "  months old")
        year=int(E2.get())
        y=str(2020-year)
        L5.configure(text="You are  " + y +" years")

    else:
        
        W3=int(month-M)
        WW=int(W3*-1)
        L4.configure(text= str(WW)  + "  months old")
        year=int(E2.get())
        y=str(2021-year)
        L5.configure(text="You are  " + y +" years")

    
L6732=Label(game,text="AGE CALCULATOR",bg="light blue",fg="Green")
L6732.pack()
       
L1=Label(game,text="Enter year-")
L1.pack()

        
E2=Entry(game)
E2.pack()


L2=Label(game,text="Enter month-")
L2.pack()

E3=Entry(game)
E3.pack()

L3=Label(game,text="Enter date-")
L3.pack()

E4=Entry(game)
E4.pack()

L5=Label(game)
L5.pack()

L4=Label(game)
L4.pack()



B1=Button(game,text="CLICK TO FIND YOUR AGE !!!!",bg="Light Blue")
B1.bind("<Button-1>",message)
B1.pack()


          
game.mainloop()

 



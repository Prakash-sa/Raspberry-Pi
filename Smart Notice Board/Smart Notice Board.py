from Tkinter import *

window=Tk()
window.title("Smart Notice Board")
window.geometry("320x240")

canvas = Canvas(window, width=350, height=400)

#img = PhotoImage(file = "smart_notice.png")
#label = Label(window, image = img)
#label.grid()

l1=Label(window,text="1.",bd=0,font=("Arial Bold",10)).grid(column=0,row=0,padx=1,pady=1)
l11=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=0,padx=1,pady=1)

l2=Label(window,text="2.",bd=0,font=("Arial Bold",10)).grid(column=0,row=2,padx=1,pady=1)
l21=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=2,padx=1,pady=1)


l3=Label(window,text="3.",bd=0,font=("Arial Bold",10)).grid(column=0,row=4,padx=1,pady=1)
l31=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=4,padx=1,pady=1)


l4=Label(window,text="4.",bd=0,font=("Arial Bold",10)).grid(column=0,row=6,padx=1,pady=1)
l41=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=6,padx=1,pady=1)


l5=Label(window,text="5.",bd=0,font=("Arial Bold",10)).grid(column=0,row=8,padx=1,pady=1)
l51=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=8,padx=1,pady=1)


l6=Label(window,text="6.",bd=0,font=("Arial Bold",10)).grid(column=0,row=10,padx=1,pady=1)
l61=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=10,padx=1,pady=1)


l7=Label(window,text="7.",bd=0,font=("Arial Bold",10)).grid(column=0,row=12,padx=1,pady=1)
l71=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=12,padx=1,pady=1)


l8=Label(window,text="8.",bd=0,font=("Arial Bold",10)).grid(column=0,row=14,padx=1,pady=1)
l81=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=14,padx=1,pady=1)


l9=Label(window,text="9.",bd=0,font=("Arial Bold",10)).grid(column=0,row=16,padx=1,pady=1)
l91=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=16,padx=1,pady=1)

l10=Label(window,text="10.",bd=0,font=("Arial Bold",10)).grid(column=0,row=18,padx=1,pady=1)
l101=Label(window,text="i am heare",bd=0,font=("Arial Bold",10)).grid(column=3,row=18,padx=1,pady=1)

window.mainloop()


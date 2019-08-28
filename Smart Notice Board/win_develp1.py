from Tkinter import *
from PIL import Image,ImageTk
from time import sleep
import firebase_admin
from firebase_admin import credentials,db,storage
import os, sys



def foo(window):
    window.update()
    name="hifjk"
    for i in range(1,10+1):
        Label(window,text=str(i)+". "+"Hi ftfjng d fjg   njnfg fh ern sdnfjd" ,wraplength=300,bg="#ffc46d",justify=LEFT,bd=0,anchor="nw",font=("Arial Bold",11)).grid(column=3,row=2*i-2,padx=1,pady=1)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,"hi",'baby','google.com')).place(x=253,y=21*(i-1)+1)
     


def b2_click(link):
    print(str(link))


def b1_click(window,text,name,link):
    window1=Toplevel(window)
    window1.title("More")
    window1.geometry("320x240")
    window1.configure(background="#00ffff")
    label = Label(window1, text=str(text)+" :- "+str(name),wraplength=300,bg="#ffc46d",justify=LEFT,bd=0,anchor="nw",font=("Arial Bold",10)).pack()
    Button(window1,text="Read",anchor='w',justify=LEFT,command=lambda:b2_click(link)).pack()
        
    while True:
        foo(window)
        sleep(0.5)
    
    
def develop_win(window):
    window1=Toplevel(window)
    window1.title("Developers")
    window1.geometry("320x240")
    window1.configure(background="#00ffff")
        
    mainmenu=Menu(window1)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home",command=window1.destroy)
    m1.add_separator()
    m1.add_command(label="Exit",command=window1.destroy)
    
    #Menu 2
#    m2=Menu(mainmenu,tearoff=0)
#    m2.add_command(label="Developers")
    
    window1.config(menu=mainmenu)
    mainmenu.add_cascade(label="More",menu=m1)
   # mainmenu.add_cascade(label="About",menu=m2)
    
    
    label1 = Label(window1, text=" Name:Ankit Gupta \n Roll No:U17EC157 ",bd=5)
    label2 = Label(window1, text=" Name:Antriksh Ganjoo \n Roll No:U17EC134 ",bd=5)
    label3 = Label(window1, text=" Name:Dhvanil Vadher \n Roll No:U17CO009 ",bd=5)
    label4 = Label(window1, text=" Name:Prakash Saini \n Roll No:U17EC151 ",bd=5)
    label1.pack()
    label2.pack()
    label3.pack()
    label4.pack()
    
    while True:
        foo(window)
        sleep(0.5)
    
    
    
    

def main():
    window=Tk()
    window.title("Smart Notice Board")
    window.geometry("320x240")
    mainmenu=Menu(window)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home")
    m1.add_separator()
    m1.add_command(label="Exit",command=window.destroy)
    
    #Menu 2
    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label="Developers",command=lambda:develop_win(window))
    
    window.config(menu=mainmenu)
    mainmenu.add_cascade(label="More",menu=m1)
    mainmenu.add_cascade(label="About",menu=m2)
    
    #background image
    image=Image.open("smart.jpg")
    photo=ImageTk.PhotoImage(image)
    Label(image=photo).place(x=0, y=0, relwidth=1, relheight=1)
    
    while True :
        foo(window)
        sleep(0.5)

    

if __name__=="__main__":
    main()

from Tkinter import *
from PIL import Image,ImageTk
from time import sleep
import firebase_admin
from firebase_admin import credentials,db,storage
import os, sys
from pathlib import Path


#firebase init

cred = credentials.Certificate('smart-notice-board-68568-firebase-adminsdk-bobtx-449e4f1790.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-notice-board-68568.firebaseio.com/'
})
root = db.reference("Transaction")

#firebase end


def foo(window):
    
    datas=root.order_by_key().get()
    Type2=[]
    Link2=[]
    Heading2=[]
    Text2=[]
    name2=[]
    LinkName2=[]
        
    datas=root.order_by_key().get()
    for data in datas:
        Text2.append(datas[data]['Text'])
        Link2.append(datas[data]['Link'])
        Type2.append(datas[data]['Type'])
        Heading2.append(datas[data]['Heading'])
        name2.append(datas[data]['name'])
        LinkName2.append(datas[data]['LinkName'])
    Type=[]
    Link=[]
    Heading=[]
    Text=[]
    name=[]
    LinkName=[]
    if Type!=Type2:
        Type=Type2
    else:
        pass
    if Link!=Link2:
        Link=Link2
    else:
        pass
    if Heading!=Heading2:
        Heading=Heading2
    else:
        pass
    if Text!=Text2:
        Text=Text2
    else:
        pass
    if name!=name2:
        name=name2
    else:
        pass
    if LinkName!=LinkName2:
        LinkName=LinkName2
    else:
        pass
    
    name="hifjk"
    sleep(0.1)
    for i in range(1,len(Heading)+1):
        
        Label(window,text=str(i)+". "+str(Heading[len(Heading)-i] ),wraplength=300,bg="#ffc46d",justify=LEFT,bd=0,anchor="nw",font=("Arial Bold",11)).grid(column=3,row=2*i-2,padx=1,pady=1)
        sleep(0.01)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-1],Link[len(Link)-1],LinkName[len(LinkName)-1],Type[len(Type)-1])).place(x=253,y=1)
        
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-2],Link[len(Link)-2],LinkName[len(LinkName)-2],Type[len(Type)-2])).place(x=253,y=22)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-3],Link[len(Link)-3],LinkName[len(LinkName)-3],Type[len(Type)-3])).place(x=253,y=43)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-4],Link[len(Link)-4],LinkName[len(LinkName)-4],Type[len(Type)-4])).place(x=253,y=64)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-5],Link[len(Link)-5],LinkName[len(LinkName)-5],Type[len(Type)-5])).place(x=253,y=85)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-6],Link[len(Link)-6],LinkName[len(LinkName)-6],Type[len(Type)-6])).place(x=253,y=106)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-7],Link[len(Link)-7],LinkName[len(LinkName)-7],Type[len(Type)-7])).place(x=253,y=127)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-8],Link[len(Link)-8],LinkName[len(LinkName)-8],Type[len(Type)-8])).place(x=253,y=148)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-9],Link[len(Link)-9],LinkName[len(LinkName)-9],Type[len(Type)-9])).place(x=253,y=168)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-10],Link[len(Link)-10],LinkName[len(LinkName)-10],Type[len(Type)-10])).place(x=253,y=190)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-11],Link[len(Link)-11],LinkName[len(LinkName)-11],Type[len(Type)-11])).place(x=253,y=211)
        sleep(0.01)
        Button(window,text="...more",fg="red",font=("Arial Bold",9),command=lambda:b1_click(window,Text[len(Text)-12],Link[len(Link)-12],LinkName[len(LinkName)-12],Type[len(Type)-12])).place(x=253,y=232)
    sleep(0.1)
    window.update()    
        
        
     


def b2_click(link,linkname1):
    p = Path('.')
    e=0
    linkname=linkname1+'?alt=media'
    for name in p.glob(linkname):
        e=1
    if e==0:
        k=os.system("wget "+str(link))
        
        sleep(5)
        os.system("evince "+str(linkname))
        
    else :
        os.system("evince "+str(linkname))
        
     
def b3_click(link,linkname1):
    p = Path('.')
    e=0
    linkname=linkname1+'?alt=media'
    for name in p.glob(linkname):
        e=1
    if e==0:
        k=os.system("wget "+str(link))
        
        sleep(5)
        os.system("gpicview "+str(linkname))
        
    else :
        os.system("gpicview "+str(linkname))
        
        

def b1_click(window,text,link,linkname,type):
    window1=Toplevel(window)
    window1.title("More")
    window1.geometry("320x240")
    window1.configure(background="#00ffff")
    label = Label(window1, text=str(text),wraplength=300,bg="#ffc46d",justify=LEFT,bd=0,anchor="nw",font=("Arial Bold",10)).pack()
    if link!='null':
        if type == '2':
            Button(window1,text="Read",anchor='w',justify=LEFT,command=lambda:b2_click(link,linkname)).pack()
        else :
            pass
        if type == '1':
            Button(window1,text="View",anchor='w',justify=LEFT,command=lambda:b3_click(link,linkname)).pack()
            
        
    
    main(window)
#    while True:
#        
#        foo(window)
#        sleep(1)
    
    
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
    
    main(window)
#    while True:
#        foo(window)
#        sleep(1)
#    
    
    
    

def main(window):
    
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
        sleep(1)

    

if __name__=="__main__":
    window=Tk()
    main(window)


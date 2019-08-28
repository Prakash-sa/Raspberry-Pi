from Tkinter import *
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials,db,storage
from time import sleep

#firebase init

cred = credentials.Certificate('smart-notice-board-68568-firebase-adminsdk-bobtx-449e4f1790.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-notice-board-68568.firebaseio.com/'
})
root = db.reference("Transaction")

#firebase end

def b1_click(url):
    #webbrowser.open_new_tab(url)
    print('hi')



def develop_win(window):
    
    window.title("Developers")
    window.geometry("320x240")
        
    mainmenu=Menu(window)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home",command=lambda:main(window))
    m1.add_command(label="Pdf",command=lambda:pdf_win(window))
    m1.add_command(label="Image",command=lambda:img_win(window))
    m1.add_separator()
    m1.add_command(label="Exit",command=window.destroy)
    
    #Menu 2
    m2=Menu(mainmenu,tearoff=0)
    m2.add_command(label="Developers")
    
    window.config(menu=mainmenu)
    mainmenu.add_cascade(label="More",menu=m1)
    mainmenu.add_cascade(label="About",menu=m2)
    
    #background image
    image=Image.open("smart.jpg")
    photo=ImageTk.PhotoImage(image)
    Label(image=photo).place(x=0, y=0, relwidth=1, relheight=1)
       
    window.mainloop()


def pdf_win(window):
    window.title("Pdf")
    window.geometry("320x240")
        
    mainmenu=Menu(window)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home",command=lambda:main(window))
    m1.add_command(label="Pdf")
    m1.add_command(label="Image",command=lambda:img_win(window))
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
    
    Type=[]
    Link=[]
    Title=[]
    Text=[]
    datas=root.order_by_key().get()
    for data in datas:
       Text.append(datas[data]['Text'])
       Link.append(datas[data]['Link'])
       Type.append(datas[data]['Type'])

    if Type[len(Type)-1]=='2': 
        image1=Image.open("pdf2.png")
        photo1=ImageTk.PhotoImage(image1)
        Label(image=photo1).place(x=15,y=5)
        Label(window,text=str(Text[len(Text)-1]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=25,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-1])).place(x=28,y=81)  
    else:
        pass 

    if Type[len(Type)-2]=='2':     
        image2=Image.open("pdf2.png")
        photo2=ImageTk.PhotoImage(image2)
        Label(image=photo2).place(x=90,y=5)
        Label(window,text=str(Text[len(Text)-2]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=100,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-2])).place(x=103,y=81)
    else:
        pass     

    if Type[len(Type)-3]=='2':    
        image3=Image.open("pdf2.png")
        photo3=ImageTk.PhotoImage(image3)
        Label(image=photo3).place(x=165,y=5)
        Label(window,text=str(Text[len(Text)-3]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=175,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-3])).place(x=178,y=81)
    else:
        pass 

    if Type[len(Type)-4]=='2':    
        image4=Image.open("pdf2.png")
        photo4=ImageTk.PhotoImage(image4)
        Label(image=photo4).place(x=240,y=5)
        Label(window,text=str(Text[len(Text)-4]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=250,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-4])).place(x=253,y=81)
    else:
        pass     


    if Type[len(Type)-5]=='2':    
        image5=Image.open("pdf2.png")
        photo5=ImageTk.PhotoImage(image5)
        Label(image=photo5).place(x=15,y=111)
        Label(window,text=str(Text[len(Text)-5]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=25,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-5])).place(x=28,y=185)
    else:
        pass 

    
    if Type[len(Type)-6]=='2':
        image6=Image.open("pdf2.png")
        photo6=ImageTk.PhotoImage(image6)
        Label(image=photo6).place(x=90,y=111)
        Label(window,text=str(Text[len(Text)-6]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=100,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-6])).place(x=103,y=185)
    else:
        pass 


    if Type[len(Type)-7]=='2':
        image7=Image.open("pdf2.png")
        photo7=ImageTk.PhotoImage(image7)
        Label(image=photo7).place(x=165,y=111)
        Label(window,text=str(Text[len(Text)-7]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=175,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-7])).place(x=178,y=185)
    else:
        pass 

    
    if Type[len(Type)-8]=='2':
        image8=Image.open("pdf2.png")
        photo8=ImageTk.PhotoImage(image8)
        Label(image=photo8).place(x=240,y=111)
        Label(window,text=str(Text[len(Text)-8]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=250,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-8])).place(x=253,y=185)
    else:
        pass 

     
    
    window.mainloop()


def img_win(window):
    window.title("Image")
    window.geometry("320x240")
        
    mainmenu=Menu(window)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home",command=lambda:main(window))
    m1.add_command(label="Pdf",command=lambda:pdf_win(window))
    m1.add_command(label="Image")
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
    
    Type=[]
    Link=[]
    Title=[]
    Text=[]
    datas=root.order_by_key().get()
    for data in datas:
       Text.append(datas[data]['Text'])
       Link.append(datas[data]['Link'])
       Type.append(datas[data]['Type'])
       #datas[data]['Text'])

    if Type[len(Type)-1]=='1' and Link[len(Link)-1]!='NULL':
        image1=Image.open("img2.png")
        photo1=ImageTk.PhotoImage(image1)
        Label(image=photo1).place(x=15,y=5)
        Label(window,text=str(Text[len(Text)-1]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=25,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-1])).place(x=18,y=79)  
    else:
        pass    

    if Type[len(Type)-2]=='1' and Link[len(Link)-2]!='NULL':    
        image2=Image.open("img2.png")
        photo2=ImageTk.PhotoImage(image2)
        Label(image=photo2).place(x=90,y=5)
        Label(window,text=str(Text[len(Text)-2]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=100,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-2])).place(x=95,y=77)
    else:
        pass 

    if Type[len(Type)-3]=='1' and Link[len(Link)-3]!='NULL':        
        image3=Image.open("img2.png")
        photo3=ImageTk.PhotoImage(image3)
        Label(image=photo3).place(x=165,y=5)
        Label(window,text=str(Text[len(Text)-3]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=175,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-3])).place(x=170,y=77)
    else:
        pass 

    if Type[len(Type)-4]=='1' and Link[len(Link)-4]!='NULL':        
        image4=Image.open("img2.png")
        photo4=ImageTk.PhotoImage(image4)
        Label(image=photo4).place(x=240,y=5)
        Label(window,text=str(Text[len(Text)-4]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=250,y=53)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-4])).place(x=245,y=77)
    else:
        pass 
    

    if Type[len(Type)-5]=='1' and Link[len(Link)-5]!='NULL':    
        image5=Image.open("img2.png")
        photo5=ImageTk.PhotoImage(image5)
        Label(image=photo5).place(x=15,y=111)
        Label(window,text=str(Text[len(Text)-5]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=25,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-5])).place(x=20,y=183)
    else:
        pass 

    if Type[len(Type)-6]=='1' and Link[len(Link)-6]!='NULL':    
        image6=Image.open("img2.png")
        photo6=ImageTk.PhotoImage(image6)
        Label(image=photo6).place(x=90,y=111)
        Label(window,text=str(Text[len(Text)-6]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=100,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-6])).place(x=95,y=183)
    else:
        pass 


    if Type[len(Type)-7]=='1' and Link[len(Link)-7]!='NULL':        
        image7=Image.open("img2.png")
        photo7=ImageTk.PhotoImage(image7)
        Label(image=photo7).place(x=165,y=111)
        Label(window,text=str(Text[len(Text)-7]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=175,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-7])).place(x=170,y=183)
    else:
        pass 
    

    if Type[len(Type)-8]=='1' and Link[len(Link)-8]!='NULL':    
        image8=Image.open("img2.png")
        photo8=ImageTk.PhotoImage(image8)
        Label(image=photo8).place(x=240,y=111)
        Label(window,text=str(Text[len(Text)-8]),bd=5,anchor='nw', justify=LEFT,font=("Arial Bold",7),bg="#ffc46d").place(x=250,y=159)
        Button(window,text="Read",command=lambda:b1_click(Link[len(Link)-8])).place(x=245,y=183)
    else:
        pass 
    
    window.mainloop()
    
    
    

def main(window):
    window.title("Smart Notice Board")
    window.geometry("320x240")
    
    mainmenu=Menu(window)
    
    #Menu 1
    m1=Menu(mainmenu,tearoff=0)
    m1.add_command(label="Home")
    m1.add_command(label="Pdf",command=lambda:pdf_win(window))
    m1.add_command(label="Image",command=lambda:img_win(window))
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
    
    Type=[]
    #Link=[]
    Title=[]
    Text=[]
    Name=[]
    datas=root.order_by_key().get()
    for data in datas:
       Text.append(datas[data]['Text'])
       #Link.append(datas[data]['Link'])
       Type.append(datas[data]['Type'])
       Name.append(datas[data]['name'])
       #datas[data]['Text'])
    for i in range(1,10):
        if Text[len(Text)-i]!='NULL' :
            Label(window,text=str(i)+". ",bd=0,bg="#ffc46d",font=("Arial Bold",10)).grid(column=0,row=2*i-2,padx=1,pady=1)
            #Label(window,text=str(Text[len(Text)-i])+"  :- "+str(Name[len(Name)-i]),wraplength=300,bg="#ffc46d",anchor="w",justify=LEFT,font=("Arial Bold",10)).grid(column=1,row=2*i-2,padx=1,pady=1)
            Label(window,text=str(Text[len(Text)-i])+"  :- "+str(Name[len(Name)-i]),wraplength=300,bg="#ffc46d",anchor="w",justify=LEFT,font=("Arial Bold",10)).grid(column=3,row=2*i-2,padx=1,pady=1)
 
    
    window.mainloop()
    

if __name__=="__main__":
    window=Tk()
    main(window)

from Tkinter import *
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials,db,storage
import os, sys
import time, threading

WAIT_SECONDS = 1

def foo():
    i=i+1
    threading.Timer(WAIT_SECONDS, foo).start()
    

#firebase init

cred = credentials.Certificate('smart-notice-board-68568-firebase-adminsdk-bobtx-449e4f1790.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-notice-board-68568.firebaseio.com/'
})
root = db.reference("Transaction")

#firebase end





def b2_click(window):
    print('hi')


def main():
    window=Tk()
    window.title("Smart Notice Board")
    window.geometry("320x240")
    
    Type=[]
    Link=[]
    Heading=[]
    Text=[]
    name=[]
        
    datas=root.order_by_key().get()
    for data in datas:
        Text.append(datas[data]['Text'])
        Link.append(datas[data]['Link'])
        Type.append(datas[data]['Type'])
        Heading.append(datas[data]['Heading'])
        name.append(datas[data]['name'])
    scrollbar=Scrollbar(window)
    scrollbar.pack(side=RIGHT,fill=BOTH)
    
    
    foo()
    while i>2500:
        print("you are success")
    
    
   
#    mylist=Listbox(window,yscrollcommand=scrollbar.set,width=0,font=("Arial Bold",13),bg="#00ffff")
#    for i in range(1,len(Heading)):
#        mylist.insert(END,str(i)+". "+ str(Heading[len(Heading)-i] ))
#        Button(window,text="...more",fg="red",font=("Arial Bold",8),command=lambda:b1_click(window,Text[len(Text)-i],name[len(name)-i],Link[len(Link)-i])).place(x=238,y=19*(i-1)+1)
# 
#    mylist.pack( side = LEFT, fill = BOTH )
#    scrollbar.config( command = mylist.yview )

    window.mainloop()
    

if __name__=="__main__":
    main()


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import sleep
from firebase_admin import storage
import os,sys


# Fetch the service account key JSON file contents
cred = credentials.Certificate('smart-notice-board-68568-firebase-adminsdk-bobtx-449e4f1790.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-notice-board-68568.firebaseio.com/'
})
root = db.reference("Transaction")
# Add a new user under /users.
#new_user = root.child('users').push({
#    'name' : 'Mary Anning', 
#    'since' : 1700
#})
#snapshot = root.order_by_key().get()
#for key, val in snapshot.items():
#    print(val)
##    pass
#    #print('{0} was {1} meters tall'.format(key, val))
#datas=root.order_by_key().get()
#print(datas)
#for val in vals:
#    print(vals[val]['Text'])
while True:
    datas=root.order_by_key().get()
    Type2=[]
    Link2=[]
    Heading2=[]
    Text2=[]
    name2=[]
        
    datas=root.order_by_key().get()
    for data in datas:
        Text2.append(datas[data]['Text'])
        Link2.append(datas[data]['Link'])
        Type2.append(datas[data]['Type'])
        Heading2.append(datas[data]['Heading'])
        name2.append(datas[data]['name'])
    Type=[]
    Link=[]
    Heading=[]
    Text=[]
    name=[]
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

#    for i in range(1,len(Heading)+1):
#        print(str(Heading[len(Heading)-i])+" "+str(Text[len(Heading)-i])+" "+str(Link[len(Link)-i])+" "+str(name[len(name)-i])+" "+str(len(Type)))
#    
    print("wget "+str(Link[len(Link)-1]))    
    sleep(0.5)


#firebase_admin.initialize_app(cred, {
#    'storageBucket': 'smartnoticeboard-f0a26.appspot.com'
#})

#buckets = storage.bucket('smartnoticeboard-f0a26')
#print(buckets)
#blob=buckets.blob('abc.pdf')
#print(blob)




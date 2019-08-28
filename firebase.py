import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


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
datas=root.order_by_key().get()
#print(datas)
#for val in vals:
#    print(vals[val]['Text'])
for data in datas:
    print(datas[data]['Text'])

#firebase_admin.initialize_app(cred, {
#    'storageBucket': 'smartnoticeboard-f0a26.appspot.com'
#})

#buckets = storage.bucket('smartnoticeboard-f0a26')
#print(buckets)
#blob=buckets.blob('abc.pdf')
#print(blob)




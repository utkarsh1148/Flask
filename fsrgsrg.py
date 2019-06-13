import smtplib
import pyrebase

config={
    "apiKey": "AIzaSyDiItwKwCkaoxjdKz8Mtbj53pBgjCutxtU",
    "authDomain": "golf-trail-8ae58.firebaseapp.com",
    "databaseURL": "https://golf-trail-8ae58.firebaseio.com",
    "projectId": "golf-trail-8ae58",
    "storageBucket": "golf-trail-8ae58.appspot.com",
    "messagingSenderId": "946041798814",
    "appId": "1:946041798814:web:8c686e4ec4f78ddb"
    }

firebase=pyrebase.initialize_app(config)
db=firebase.database()
storage=firebase.storage()

velocity=db.child("Velocity").get()
v = velocity.val()
v=v.values()
v=str(v)

mh=db.child("Max_Height").get()
h = mh.val()
h=h.values()
h=str(h)

ran=db.child("Range").get()
r = ran.val()
r=r.values()
r=str(r)

ang=db.child("Theta").get()
a = ang.val()
a=a.values()
a=str(a)

FP=db.child("FPS").get()
f = FP.val()
f=f.values()
f=str(f)

dict_=[f,v,h,r,a]
string='Frame Rate:'+  f + '\n' + "Maximum Height:" + h+'\n '+ "Angle:" + a +'\n' + "Velocity :"+ v + '\n' + "Range:"+r

content=string

mail=smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('utkarsh1148@gmail.com','1401utkarsh2000')

mail.sendmail('utkarsh1148@gmail.com','priyankautk1@gmail.com',content)

mail.close( )



import pyrebase
from flask import *


config={
    "apiKey": "AIzaSyDiItwKwCkaoxjdKz8Mtbj53pBgjCutxtU",
    "authDomain": "golf-trail-8ae58.firebaseapp.com",
    "databaseURL": "https://golf-trail-8ae58.firebaseio.com",
    "projectId": "golf-trail-8ae58",
    "storageBucket": "golf-trail-8ae58.appspot.com",
    "messagingSenderId": "946041798814",
    "appId": "1:946041798814:web:472b1460c77ca90e"
    }

firebase=pyrebase.initialize_app(config)
db=firebase.database()
storage=firebase.storage()


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def basic():
    if request.method=="POST":
        name=request.form['name']
        db.child("todo").push(name)
        todo=db.child("todo").get()
        to = todo.val()
        print(to.values())
        return render_template('hello.html', t=to.values())    
    return render_template("hello.html")

if __name__=='__main__':
    app.run(debug=True)



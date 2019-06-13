
import pyrebase
from flask import *


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





app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def basic():
    if request.method=='POST':
        upload=request.files['upload']
        storage.child("images/new.mp4").put(upload)
        return redirect(url_for('uploads'))
    return render_template("hi.html")

@app.route("/uploads")
def uploads():
    import final_show
    if True:
        links=storage.child("images/new.mp4").get_url(None)
        return render_template('upload.html',l=links)
    


if __name__=="__main__":
    app.run(debug=True)

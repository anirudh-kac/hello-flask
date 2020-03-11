from flask import Flask,session,redirect,render_template,url_for,flash,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
 #set the URI for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fruits.sqlite3'

db = SQLAlchemy(app)

class Fruits(db.Model):
    _id = db.Column("Id",db.Integer(),primary_key = True)
    name = db.Column("Name",db.String(100))
    #rating = db.Column("Rating",db.Integer)

    def __init__(self,name ):
        self.name = name
        #self.rating = rating


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    else:
        fruit = Fruits(request.form["name"])
        db.session.add(fruit)
        db.session.commit()
        return redirect(url_for("view"))

@app.route("/view")
def view():
    fruits = None
    fruits = Fruits.query.all()
    return render_template("view.html",fruits = fruits)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

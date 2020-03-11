from flask import Flask,session,redirect,render_template,url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
 #set the URI for the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fruits.sqlite3'

db = SQLAlchemy(app)

class Fruits(db.Model):
    name = db.Column("Name",db.String(100))
    rating = db.Column("Rating",db.Integer)

    def __init__(self,name,rating):
        self.name = name
        self.rating = rating



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

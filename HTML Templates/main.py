from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html",name = "Fun",services = ["Jokes","Sarcasm","Memes"])

@app.route("/<user_name>")
def user(user_name):
    return render_template("user.html",user = user_name)

if __name__ == "__main__":
    app.run()


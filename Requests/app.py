from flask import Flask,redirect,render_template,request,url_for

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "GET" :
        return render_template("login.html")
    else:
        username = request.form["name"]
        return redirect(url_for("user",user = username))

@app.route("/<user>")
def user(user):
    return render_template("user.html",name= user)


if(__name__ == "__main__"):
    app.run(debug=True)
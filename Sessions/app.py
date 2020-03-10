from flask import Flask,session,request,render_template,url_for,redirect
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
# set duration for  a session
app.permanent_session_lifetime = timedelta(minutes = 5)



@app.route("/",methods = ["POST","GET"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        session.permanent = True
        name = request.form["name"]
        session["name"] = name
        return redirect(url_for("profile"))


@app.route("/profile")
def profile():
    if "name" in session:
        return render_template("profile.html",name = session["name"])
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask , redirect , url_for

#create an instance of flask app
app = Flask(__name__)

# use @app.route decorator
@app.route("/")
def home():
    return "Hello there, welcome to the flask app"



# HTML can be sent using return
@app.route("/about")
def about():
    return "<h1> This is a demo Flask app </h1>"


@app.route("/users/<name>")
def user(name):
    return f"<h1> Hello {name}"


admin_access = False

# to redirect , use the redirect function , passing url_for with function name in quotes
@app.route("/admin")
def admin():
    if(admin_access):
        return "Hello Admin"
    else:
        return redirect(url_for("home"))
if __name__ == "__main__":
    app.run()

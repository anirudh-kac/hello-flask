from flask import Flask , redirect , url_for

#create an instance of flask app
app = Flask(__name__)

# use @app.route decorator
@app.route("/")
def home():
    return "Hello there, welcome to the flask app"

if __name__ == "__main__":
    app.run()

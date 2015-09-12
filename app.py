from flask import Flask
app = Flask(__name__)

@app.route("/about")
def hello():
    return "Hello World!"

@app.route("/poop")
def poop():
	return "<h1> poop </h1><h2> poop never again </h2>"

if __name__ == "__main__":
    app.run()
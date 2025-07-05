from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Abinash Maharana", year=datetime.now().year)

@app.route("/about")
def about():
    return render_template("about.html", title="About Me", year=datetime.now().year)

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Me", year=datetime.now().year)

@app.route("/projects")
def projects():
    return render_template("projects.html", title="My Projects", year=datetime.now().year)

if __name__ == "__main__":
    app.run(debug=True)
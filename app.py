from flask import Flask, redirect, url_for, render_template, request
from datetime import date


app = Flask(__name__)

@app.route("/")
def home():
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    print(d1)
    return render_template("mainPage.html", d1=d1)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        job = request.form["job"]
        questions = request.form['number']
        print(job)
        print(questions)

        return render_template("interview.html", 
        job=job
        )
    else:
	    return render_template("login.html")


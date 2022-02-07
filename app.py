from flask import Flask, render_template, request
from datetime import date
import smtplib


app = Flask(__name__)

@app.route("/")
def home():
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    print(d1)
    return render_template("mainPage.html", d1=d1)


@app.route("/login", methods=["POST"])
def login():
    return render_template("login.html")

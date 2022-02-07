from flask import Flask, render_template
from datetime import date





app = Flask(__name__)

@app.route("/")
def home():
    today = date.today()
    d1 = today.strftime("%B %d, %Y")
    print(d1)
    return render_template("mainPage.html", d1=2)
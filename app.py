from flask import Flask, redirect, url_for, render_template, request
from datetime import date
import os
import openai
import json
import requests
openai.api_key = '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'


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

        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"Create a list of {questions} questions for my interview as a {job}\n",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)
        text = response.choices[0].text
        print(text)        


        return render_template("interview.html", 
        text=text
        )

    else:
	    return render_template("login.html")


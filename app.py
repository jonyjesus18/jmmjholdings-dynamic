from flask import Flask, redirect, url_for, render_template, request
from datetime import date
import os
import openai
import json
import requests
key1 = 'sk-YQtgOUqZXkJ8oFLzORo2T3'
key2 = 'BlbkFJ7RbBtMo9KMz6RKXt2VbA'
openai.api_key = f"{key1}{key2}"


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
        experience = request.form['experience']
        print(job)
        print(experience)

        response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"Create a list of 8 questions for my interview as a {experience} {job}\n",
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)
        text = response.choices[0].text
        print(text)
        list = text.split('\n')[1:]
        list = filter(None, list)
        # list = ["sfsdgfsegds","sfsargsgd","sefsargsrgdsr"]

        return render_template("interview.html", 
        list=list
        )

    else:
	    return render_template("login.html")



@app.route("/joinMailingList", methods=["POST", "GET"])
def joinMailingList():
	return render_template("joinMailingList.html")



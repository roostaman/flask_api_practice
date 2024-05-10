from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


def get_age(username):
    response = requests.get(url=f"https://api.agify.io?name={username}")
    age = response.json()["age"]
    return age


def get_gender(username):
    response = requests.get(url=f"https://api.genderize.io?name={username}")
    gender = response.json()["gender"]
    return gender


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    date = datetime.now().strftime("%Y")
    return render_template("index.html", username="username", age=random_number,
                           date=date, gender="gender")


@app.route("/<username>")
def random_name(username):
    date = datetime.now().strftime("%Y")
    age = get_age(username)
    gender = get_gender(username)
    username = username.title()
    return render_template("index.html", date=date, username=username, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)


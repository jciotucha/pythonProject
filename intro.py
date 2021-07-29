import sqlite3
from datetime import timedelta

from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


@app.route("/baza")
def square():
    return str(2 * 2)
    return render_template("baza.html")


@app.route("/baza2")
def square2():
    con = sqlite3.connect('test2.db')
    cur = con.cursor()
    word = (cur.execute('SELECT * from slow1'))
    return print(word.fetchall())
    return render_template("baza2.html", word=word)

@app.route("/agent")
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p> Twoja przeglądarka to {}</p>'.format(user_agent)


# print(square2())

# app.jinja_env.globals.update(square2=square2)

if __name__ == "__main__":
    app.run(debug=True)
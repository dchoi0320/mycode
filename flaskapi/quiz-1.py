#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    #return render_template("postmaker.html")
    return render_template("quiz-1.html")

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect("/correct")
            else:
                return redirect("/")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

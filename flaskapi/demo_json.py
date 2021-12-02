#!/usr/bin/python3
"""DAY 4 - DEMO: posting JSON, receiving JSON"""

from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

jsondata = []   # empty list

# ONLY posts to /post
app.route("/post", methods=["POST"])
def post():
    # request.form    # what am I trying to access? accessing data from the post (submitted via HTML)
    # request.args    # accessing data from query params (?name=David)
    # request.method  # accessing what thpe of request method was used (GET, POST)
    # request.json    # accessing JSON attached to the post

    data = request.json
    # data now contains JSON submitted by the client

    # if JSON was actually sent:
    if data:
        # treat 'data' like a dictionary.
        nm = data["name"]
        ic = data["ice cream"]
        color = data["color"]
        jsondata.append({"nm": nm, "ic": ic, "color": color})
    return redirect("/")

    @app.route("/")
    def index():
        # how to have a Flask API return object as JSON
        #return jsondata
        return jsonify(jsondata)
    
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=2224)
        
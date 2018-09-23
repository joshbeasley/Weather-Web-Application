import os
import re
from flask import Flask, jsonify, render_template, request, url_for


from cs50 import SQL




# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

         # gets q from html page
        q = request.args.get("q") + "%"

        # query the database for inputed place
        places = db.execute(
            "SELECT * FROM places WHERE postal_code LIKE :q OR place_name LIKE :q OR admin_name1 LIKE :q", q=q)

    return render_template("index.html")

from flask import Flask, jsonify, request, render_template, redirect, url_for
import json
import pymongo
from pymongo.errors import PyMongoError

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://shaqibshaikh1911:ft3NEmEeu097FcXa@mongocluster.87ti7yy.mongodb.net/?retryWrites=true&w=majority")
db = client["flaskdb"]
collection = db["users"]


@app.route("/api")
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data)

@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except PyMongoError as e:
            error = str(e)
    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

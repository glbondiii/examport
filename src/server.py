import atexit
import sqlite3
import sqldb
from flask import Flask, jsonify
from question import Question

app: Flask = Flask(__name__)
db: sqlite3.Connection

@app.route("/")
@app.route("/init")
@app.route("/init/<courseID>")
def init(courseID: str = ""):
    global db
    if (courseID == ""):
        return "Enter the course ID for your exam in the URL (e.g localhost:5000/init/[courseID])"
    path = input("Enter the absolute path where your databases are: ")
    db = sqldb.connectToDatabase(path, courseID)
    return f"Set database to {courseID} at {path}"

@app.route("/select/random")
def getRandomQuestion():
    randQuestion: Question = sqldb.getRandomQuestion(db)
    return jsonify(randQuestion)


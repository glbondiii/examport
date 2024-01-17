import sqlite3
import sqldb
from flask import Flask, jsonify
from question import Question

app: Flask = Flask(__name__)
path: str = ""
db: sqlite3.Connection

@app.route("/")
@app.route("/init")
@app.route("/init/<courseID>")
def init(courseID: str = ""):
    global path
    global db
    if (path == ""):
        path = input("Enter the absolute path where your databases are: ")
    if (courseID == ""):
        return "Enter the course ID for your exam in the URL (e.g localhost:5000/init/[courseID])"
    db = sqldb.connectToDatabase(path, courseID)
    return f"Set database to {courseID} at {path}"

@app.route("/select/random")
def getRandomQuestion():
    randQuestion: Question = sqldb.getRandomQuestion(db)
    return jsonify(randQuestion)

@app.route("/select/random/<questionTypeStr>")
def getRandomQuestionType(questionTypeStr: str):
    questionType: int = int(questionTypeStr)
    randQuestion: Question = sqldb.getRandomQuestion(db, questionType)
    return jsonify(randQuestion)

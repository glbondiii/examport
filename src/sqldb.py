import os
import sqlite3
from question import Question, question_types

def connectToDatabase(path: str, courseID: str) -> sqlite3.Connection:
    newDB: bool = False
    dbPath = f"{path}/{courseID}.db"

    if (not os.path.isfile(dbPath)):
        newDB = True

    print(newDB)
    db: sqlite3.Connection = sqlite3.connect(dbPath)

    if (newDB):
        db.execute("""CREATE TABLE users (
            name TEXT,
            password TEXT,
            admin INTEGER,
            excludeAnswered INTEGER
            )""") # Create users table

        db.execute("""CREATE TABLE questions (
            exam_semester TEXT,
            exam_unit INTEGER,
            question_num INTEGER,
            type TEXT,
            given TEXT,
            explanation TEXT,
            answer TEXT,
            possible_answers TEXT,
            users_answered TEXT
            )""") # Create questions table

    return db

def addQuestionsToDatabase(questions: list[Question], db: sqlite3.Connection):
    for question in questions:
        questionDict: dict = question.__dict__
        print(tuple(questionDict.values()))
        db.execute("""INSERT INTO questions (exam_semester, exam_unit, question_num, type, given, 
                                             explanation, answer, possible_answers, users_answered) 
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
                   tuple(questionDict.values()))
        db.commit()

def getRandomQuestion(db: sqlite3.Connection) -> Question:
    questions: list[Question] = []

    questionSQL: list = db.execute("SELECT * from questions ORDER BY random()").fetchall()

    for question in questionSQL:
        newQuestion: Question = Question(question[0], question[1], question[2], question[3],
                                         question[4], question[5], question[6], question[7],
                                         question[8])
        questions.append(newQuestion)

    index: int = 0
    # Increment index until reach last question or question that hasnt been answered yet

    return questions[index]


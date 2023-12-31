import sqlite3
import sqldb
import script
from question import Question

def main():
    print("ExamPort for StudyBinder (into SQL format)\n")
    path_to_databases: str = input("Enter the absolute path where your databases are: ")
    courseID: str = input("Enter the course ID for your exam: ")
    db: sqlite3.Connection = sqldb.connectToDatabase(path_to_databases, courseID)
    questions: list[Question] = script.getExamQuestions()
    sqldb.addQuestionsToDatabase(questions, db)
    if db:
        db.close()

if __name__ == "__main__":
    main()


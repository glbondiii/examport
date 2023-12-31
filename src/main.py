import sqlite3
import sqldb
import script
from question import Question

def main():
    print("ExamPort for StudyBinder (into SQL format)\n")
    isScript: bool = True
    path_to_databases: str = input("Enter the absolute path where your databases are: ")
    courseID: str = input("Enter the course ID for your exam: ")
    db: sqlite3.Connection = sqldb.connectToDatabase(path_to_databases, courseID)
    if db: 
        if isScript:
            questions: list[Question] = script.getExamQuestions()
            sqldb.addQuestionsToDatabase(questions, db)
            db.close()
        else:
            # Start HTTP Server here
            pass

if __name__ == "__main__":
    main()


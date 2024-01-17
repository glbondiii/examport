import sqlite3
import sqldb
from question import Question, question_types

question_types: list[str] = ["Free Response", "Short Answer", "Multiple Choice", "True/False"]

def main():
    print("ExamPort Script for StudyBinder (into SQL format)\n")
    path_to_databases: str = input("Enter the absolute path where your databases are: ")
    courseID: str = input("Enter the course ID for your exam: ")
    db: sqlite3.Connection = sqldb.connectToDatabase(path_to_databases, courseID)
    questions: list[Question] = getExamQuestions()
    sqldb.addQuestionsToDatabase(questions, db)
    db.close()


def getExamQuestions() -> list[Question]:
    complete: bool = False
    questions: list[Question] = []
    index: int = -1

    semester: str = input("Exam semester: ")

    unit: int = 0
    while (unit <= 0):
        try:
            unit = int(input("Exam unit: "))
            if (unit <= 0):
                print("Input cannot be negative or zero")
        except ValueError:
            print("Cannot input a string or decimal")

    while (index <= 0):
        try:
            index = int(input("Start at question: "))
            if (index <= 0):
                print("Input cannot be negative or zero")
        except ValueError:
            print("Cannot input a string or decimal")

    while (complete == False):
        questionNum: int = index
        type: str = ""
        given: str = ""
        explanation: str = ""
        answer: str = ""
        possibleAnswers: str = ""

        print(f"Question {questionNum}:")
        
        typeIndex: int = 0
        while (typeIndex <= 0):
            try:
                printQuestionTypes()
                print(f"\nEnter the index of the type you want question {questionNum} to be")
                typeIndex: int = int(input(f"Question {questionNum} Type: "))
                if (typeIndex <= 0):
                    print("Input cannot be negative or zero")
            except ValueError:
                print("Cannot input a string or decimal")

        type = question_types[typeIndex-1]
        given = input("Question Given: ")
        print()
        explanation = input("Question Explanation: ")
        print()
        
        if (type != question_types[0]):
            if (type == question_types[2]):
                answer = input("Question Answer: ")
                possibleAnswers = possibleAnswers + f"{answer}"
                for i in range(1, 4):
                    possibleAnswer = input(f"Possible Response {i}: ")
                    possibleAnswers = possibleAnswers + f",{possibleAnswer}"

            elif (type == question_types[3]):
                while (answer != "true" and answer != "false"):
                    answer = input("Is the given true or false? (answer in lowercase) ")
                possibleAnswers = "true,false"

            else: 
                answer = input("Question Answer: ")

        question: Question = Question(semester, unit, questionNum, type, given, explanation, answer, 
                                      possibleAnswers, "")

        questions.append(question)
        index+=1

        done: str = input("Are you done inputting questions? ")

        if (done.startswith('y') or done.startswith('Y')):
            complete = True

    return questions

def printQuestionTypes(): 
    index: int = 1

    print("\nQuestion Types")
    for question_type in question_types: 
        print(f"{index}. {question_type}")
        index+=1

if __name__ == "__main__":
    main()

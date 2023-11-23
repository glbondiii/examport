import json
from question import Question, Exam

path_to_exams: str = "/home/glbondiii/Programming_Projects/examport/exams"
question_types: list[str] = ["Free Response", "Fill-in-the-Blank", "Multiple Choice", "True/False"]

def main():
    print("ExamPort for StudyBinder (in JSON format)\n")
    exam: Exam = getExamDetails()
    examDict: dict = getExamDict(exam)
    print(examDict)
    examJson: str = json.dumps(examDict)
    file = open(f"{path_to_exams}/{exam.semester}Unit{exam.unit}.json".replace(" ", ""), "w")
    file.write(examJson)
    print(f"Written to {path_to_exams}/{exam.semester.replace(' ', '')}Unit{exam.unit}.json")

def getExamDetails() -> Exam:
    semester: str = input("Exam semester: ")

    unit: int = 0
    while (unit <= 0):
        try:
            unit: int = int(input("Exam unit: "))
            if (unit <= 0):
                print("Input cannot be negative or zero")
        except ValueError:
            print("Cannot input a string or decimal")

    questions: list[Question] = getExamQuestions(semester, unit)
    
    return Exam(semester, unit, questions) 

def getExamQuestions(semester: str, unit: int) -> list[Question]:
    complete: bool = False
    questions: list[Question] = []
    index: int = 1

    while (complete == False):
        examId: str = f"{semester}, Unit {unit}" 
        examNum: int = index
        type: str = ""
        given: str = ""
        explanation: str = ""
        answer: str = ""
        possibleAnswers: list[str] = []

        print(f"Question {examNum}:")
        
        typeIndex: int = 0
        while (typeIndex <= 0):
            try:
                printQuestionTypes()
                print(f"\nEnter the index of the type you want question {examNum} to be")
                typeIndex: int = int(input(f"Question {examNum} Type: "))
                if (typeIndex <= 0):
                    print("Input cannot be negative or zero")
            except ValueError:
                print("Cannot input a string or decimal")

        type = question_types[typeIndex-1]
        given = input("Question Given: ")
        explanation = input("Question Explanation: ")
        
        if (type != question_types[0]):
            answer = input("Question Answer: ")

            if (type == question_types[2]):
                possibleAnswers.append(answer) 
                for i in range(1, 4):
                    possibleAnswer = input(f"Possible Response {i}: ")
                    possibleAnswers.append(possibleAnswer)

            if (type == question_types[3]):
                possibleAnswers = ["true", "false"]

        question: Question = Question(examId, examNum, type, given, explanation, answer, 
                                      possibleAnswers)

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

def getExamDict(exam: Exam) -> dict:
    examDict: dict = exam.__dict__

    questionsJson: list[dict] = []

    for question in exam.questions:
        questionsJson.append(question.__dict__)

    examDict["questions"] = questionsJson

    return examDict


if __name__ == "__main__":
    main()


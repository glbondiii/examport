from dataclasses import dataclass

@dataclass
class Question:
    examSemester: str
    examUnit: int
    questionNum: int
    type: str
    given: str
    explanation: str
    answer: str
    possibleAnswers: str
    usersAnswered: str

question_types: list[str] = ["Free Response", "Short Answer", "Multiple Choice", "True/False"]

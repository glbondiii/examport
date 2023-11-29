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


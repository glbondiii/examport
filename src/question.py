from dataclasses import dataclass

@dataclass
class Question:
    examId: str
    examNum: int
    type: str
    given: str
    explanation: str
    answer: str
    possibleAnswers: list[str]

@dataclass
class Exam:
    semester: str
    unit: int
    questions: list[Question]

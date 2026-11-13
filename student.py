from __future__ import annotations

from datetime import datetime


class Student:
    sMatric_number: str
    name: str
    student_level: str
    gender: str
    dob: str
    scores: dict[str, float]
    date_entered: str

  
    def __init__(self, sMatric_number: str, name: str, student_level: str, gender: str, dob: str):
        self.sMatric_number = sMatric_number
        self.name = name
        self.student_level = student_level
        self.gender = gender
        self.dob = dob            
        self.scores = {}          
        self.date_entered = ""    

    
    def set_score(self, subject: str, score: float) -> None:
        self.scores[subject] = score
        
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")


    def get_total(self) -> float:
        total = 0.0
        for subject in self.scores:
            total = total + self.scores[subject]
        return total

   
    def get_average(self) -> float:
        if len(self.scores) == 0:
            return 0.0
        return self.get_total() / len(self.scores)

 
    def to_dict(self) -> dict[str, object]:
        return {
            "sMatric_number": self.sMatric_number,
            "name": self.name,
            "student_class": self.student_level,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_entered": self.date_entered,
        }



def student_from_dict(data: dict[str, object]) -> Student:
    sMatric_number = str(data.get("sMatric_number", ""))
    name = str(data.get("name", ""))
    student_class = str(data.get("student_class", ""))
    gender = str(data.get("gender", ""))
    dob = str(data.get("dob", ""))

    s = Student(sMatric_number, name, student_class, gender, dob)

    raw_scores = data.get("scores", {})
    if isinstance(raw_scores, dict):
        scores: dict[str, float] = {}
        for key, value in raw_scores.items():
            try:
                scores[str(key)] = float(value)
            except (TypeError, ValueError):
                continue
        s.scores = scores
    s.date_entered = str(data.get("date_entered", ""))
    return s

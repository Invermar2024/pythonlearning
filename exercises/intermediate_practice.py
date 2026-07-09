students = [
    {"name": "Ana", "score": 92},
    {"name": "Luis", "score": 85},
    {"name": "Mia", "score": 78},
    {"name": "Tom", "score": 58},
]

passing_students = [student for student in students if student["score"] >= 60]
names_by_score = {
    student["name"]: student["score"]
    for student in sorted(students, key=lambda item: item["score"], reverse=True)
}


class StudySession:
    def __init__(self, topic, minutes):
        self.topic = topic
        self.minutes = minutes

    def summary(self):
        return f"{self.topic}: {self.minutes} minutes"


sessions = [
    StudySession("comprehensions", 25),
    StudySession("classes", 35),
]

print("Passing students:")
for student in passing_students:
    print(f"- {student['name']}")

print("\nScores:")
print(names_by_score)

print("\nStudy sessions:")
for session in sessions:
    print(session.summary())

class Course:
    def __init__(self, title):
        self.title = title
        self.lessons = []

    def add_lesson(self, lesson_title):
        self.lessons.append({"title": lesson_title, "completed": False})

    def complete_lesson(self, lesson_title):
        for lesson in self.lessons:
            if lesson["title"] == lesson_title:
                lesson["completed"] = True
                return True
        return False

    def progress(self):
        if not self.lessons:
            return 0

        completed = 0

        for lesson in self.lessons:
            if lesson["completed"]:
                completed += 1

        return completed / len(self.lessons)

    def summary(self):
        percent = self.progress() * 100
        return f"{self.title}: {percent:.0f}% complete"


python_course = Course("Intermediate Python")
python_course.add_lesson("Comprehensions")
python_course.add_lesson("Object-oriented programming")
python_course.add_lesson("Testing")

python_course.complete_lesson("Comprehensions")
python_course.complete_lesson("Object-oriented programming")

print(python_course.summary())

for lesson in python_course.lessons:
    status = "done" if lesson["completed"] else "pending"
    print(f"- {lesson['title']}: {status}")

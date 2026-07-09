notes = [
    "Practice variables",
    "Review loops",
    "Create a small project",
]

with open("study_notes.txt", "w", encoding="utf-8") as file:
    for note in notes:
        file.write(note + "\n")

with open("study_notes.txt", "r", encoding="utf-8") as file:
    saved_notes = [line.strip() for line in file]

print("Saved notes:")

for note in saved_notes:
    print(f"- {note}")

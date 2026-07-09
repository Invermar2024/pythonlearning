def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_passing(grade):
    return grade >= 60


grades = [80, 55, 92, 60, 48]

print(f"Average grade: {calculate_average(grades)}")

for grade in grades:
    if is_passing(grade):
        print(f"{grade}: pass")
    else:
        print(f"{grade}: review")

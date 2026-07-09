numbers = [3, 6, 9, 12, 15]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

total = 0

for number in numbers:
    total += number

print(f"Total: {total}")
print(f"Average: {total / len(numbers)}")

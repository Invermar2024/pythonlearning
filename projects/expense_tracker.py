import csv
from pathlib import Path


FILE_PATH = Path("expenses.csv")


def add_expense():
    description = input("Description: ").strip()
    amount_text = input("Amount: ").strip()

    try:
        amount = float(amount_text)
    except ValueError:
        print("Amount must be a number.")
        return

    file_exists = FILE_PATH.exists()

    with FILE_PATH.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["description", "amount"])

        writer.writerow([description, amount])

    print("Expense saved.")


def show_expenses():
    if not FILE_PATH.exists():
        print("No expenses saved yet.")
        return

    total = 0

    with FILE_PATH.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])
            total += amount
            print(f"{row['description']}: {amount}")

    print(f"Total: {total}")


def main():
    while True:
        print("\n1. Add expense")
        print("2. Show expenses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

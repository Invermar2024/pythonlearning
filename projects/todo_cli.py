tasks = []


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "done" if task["done"] else "pending"
        print(f"{index}. {task['title']} - {status}")


def add_task():
    title = input("Task title: ").strip()

    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Task title cannot be empty.")


def mark_done():
    show_tasks()
    choice = input("Task number to mark done: ")

    try:
        index = int(choice) - 1
        tasks[index]["done"] = True
        print("Task updated.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Mark done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()

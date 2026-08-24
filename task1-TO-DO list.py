"""Simple command-line to-do list application."""


def display_tasks(tasks):
	if not tasks:
		print("\nYour to-do list is empty.")
		return

	print("\nTo-do list:")
	for number, task in enumerate(tasks, start=1):
		status = "✓" if task["completed"] else " "
		print(f"{number}. [{status}] {task['title']}")


def choose_task(tasks, action):
	if not tasks:
		print("There are no tasks to select.")
		return None

	display_tasks(tasks)
	try:
		number = int(input(f"Enter the task number to {action}: "))
		if 1 <= number <= len(tasks):
			return number - 1
	except ValueError:
		pass

	print("Invalid task number.")
	return None


def main():
	tasks = []

	while True:
		print("\n--- To-Do List ---")
		print("1. View tasks")
		print("2. Add task")
		print("3. Complete task")
		print("4. Delete task")
		print("5. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			display_tasks(tasks)
		elif choice == "2":
			title = input("Enter a task: ").strip()
			if title:
				tasks.append({"title": title, "completed": False})
				print("Task added.")
			else:
				print("Task cannot be empty.")
		elif choice == "3":
			index = choose_task(tasks, "complete")
			if index is not None:
				tasks[index]["completed"] = True
				print("Task completed.")
		elif choice == "4":
			index = choose_task(tasks, "delete")
			if index is not None:
				tasks.pop(index)
				print("Task deleted.")
		elif choice == "5":
			print("Goodbye!")
			break
		else:
			print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
	main()

import json

class Task:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def toggle_done(self):
        self.is_done = not self.is_done

    def __str__(self):
        return f"{'[x]' if self.is_done else '[ ]'} {self.description}"

class ToDoList:
    def __init__(self, file_name="tasks.json"):
        self.tasks = []
        self.file_name = file_name
        self.load_tasks()

    def add_task(self, description):
        self.tasks.append(Task(description))
        self.save_tasks()

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            self.save_tasks()

    def toggle_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle_done()
            self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self):
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = [Task(**data) for data in json.load(file)]
        except FileNotFoundError:
            self.tasks = []

    def list_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx}. {task}")

def main():
    todo_list = ToDoList()

    menu = """
    1. Add Task
    2. Edit Task
    3. Toggle Task Done
    4. Remove Task
    5. List Tasks
    6. Exit
    """

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            description = input("Enter task description: ").strip()
            todo_list.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to edit: ").strip())
            new_description = input("Enter new description: ").strip()
            todo_list.edit_task(index, new_description)
        elif choice == "3":
            index = int(input("Enter task index to toggle done: ").strip())
            todo_list.toggle_task_done(index)
        elif choice == "4":
            index = int(input("Enter task index to remove: ").strip())
            todo_list.remove_task(index)
        elif choice == "5":
            todo_list.list_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

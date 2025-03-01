#To-Do List

# class ToDoList:
#     def _init_(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)
#         print(f"Task '{task}' added to the list.")

#     def remove_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             print(f"Task '{task}' removed from the list.")
#         else:
#             print(f"Task '{task}' not found in the list.")

#     def view_tasks(self):
#         if not self.tasks:
#             print("No tasks in the list.")
#         else:
#             print("To-Do List:")
#             for idx, task in enumerate(self.tasks, start=1):
#                 print(f"{idx}. {task}")

# def main():
#     todo_list = ToDoList()

#     while True:
#         print("\nTo-Do List Manager")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. View Tasks")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             task = input("Enter the task: ")
#             todo_list.add_task(task)
#         elif choice == '2':
#             task = input("Enter the task to remove: ")
#             todo_list.remove_task(task)
#         elif choice == '3':
#             todo_list.view_tasks()
#         elif choice == '4':
#             print("Exiting To-Do List Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if name == "_main_":
#     main()

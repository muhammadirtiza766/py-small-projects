import os

todos = ['Dummy task']

def show_todos():
  for todo in todos:
    print(f">: {todo}")

def add_todo():
  new_todo = input('Enter new todo: ')
  todos.append(new_todo)

app = True

while app:
  usr_input = input('Enter what you want todo: ')

  if usr_input == 'add':
    add_todo()

  if usr_input == 'show':
    show_todos()

  if usr_input == 'quit':
    app = False

  if usr_input == 'remove':
    rm_element = input('Enter the element you want to delete: ')
    todos.remove(rm_element)

  if usr_input == 'cls':
    os.system('cls' if os.name == 'nt' else 'clear')
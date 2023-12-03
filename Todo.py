import re

completeCnt = 0

def listItems(filepath = '/content/drive/MyDrive/Colab Notebooks/Files/todo.txt'):
  """list items in textfile, filepath should be the path to your txt file."""
  with open(filepath, 'r') as f:
    for lineNumber, lineContent in enumerate(f, start=1):
      print(f'Item Number {lineNumber} is: {lineContent.strip()}')

def appItems(filepath = '/content/drive/MyDrive/Colab Notebooks/Files/todo.txt'): 
  """Append items to a textfile, filepath should be the path to your txt file."""
  with open(filepath, 'a') as f:
    f.write(f'{todo.strip()}\n')

def readLines(filepath = '/content/drive/MyDrive/Colab Notebooks/Files/todo.txt'):
  """Read all lines in a text file and store return them as output"""
  with open(filepath, 'r') as f:
    y = f.readlines()
  return y

def writeList(y, filepath = '/content/drive/MyDrive/Colab Notebooks/Files/todo.txt'):
  """Open txt file at the filepath provided as argument and store them in argument y"""
  with open(filepath, 'w') as f:
    for item in y:
      f.write(f'{item.strip()}\n')


print('Your things to do are: ')
listItems()

while True:
  user_action = input('Type add, show, edit, complete, clear, help or exit: ')
  user_action = user_action.strip() #Removes whitespace before and after the string

  if user_action.startswith('add'):
    todo = user_action[3:]

    appItems()

  elif  user_action.startswith('show'):
    listItems()

  elif user_action.startswith('edit'):

    try:

      # Using regular expression to extract the number, '\d+' stands for 'digit'
      match = re.search(r'\d+', user_action)

      if match:
          changeNum = match.group()
      else:
          print("You must give the number of the todo you want to change")

      newTodo = user_action.replace('edit', '')
      newTodo = newTodo.replace(changeNum,'')

      content  = readLines()

      # Change the specific string
      content[int(changeNum)-1] = newTodo

      # Write the modified content back to the file
      writeList(content)

    except IndexError:
      print('Item is not in the list, try using the show command')
      continue

  elif user_action.startswith('complete'):

    try:

      match = re.search(r'\d+', user_action)

      if match:
          completeNum = int(match.group())
      else:
          print("You must give the number of the todo you want to complete")

      content  = readLines()

        # Delete the specific item
      content.pop(completeNum-1)

      writeList(content)

      print('Todo ' + str(completeNum) +' is complete')

      completeCnt = completeCnt + 1
      print(f'You have completed {completeCnt} todos today!')

    except IndexError:
      print('Item is not in the list, try using the show command')
      continue

  elif user_action.startswith('clear'):

    try:

      match = re.search(r'\d+', user_action)

      if match:
          clearNum = int(match.group())
      else:
          print("You must give the number of the todo you want to complete")

      clearNum = clearNum - 1

      content  = readLines('/content/drive/MyDrive/Colab Notebooks/Files/todo.txt')

      # Delete the specific item
      content.pop(clearNum)

      # Write the modified content back to the file

      writeList(content)

    except IndexError:
      print('Item is not in the list, try using the show command')
      continue

  elif user_action.startswith('help'):

    print('')
    print('Type "add YOUR_ACTION" to add a new action to your todo list')
    print('Type "show" to show your current todo list')
    print('Type "complete ACTION_NUMBER" to complete your todo')
    print('Typ "clear ACTION_NUMBER" to delete that todo')
    print('Type "exit" to exit application')
    print('')

    print('     oooo   o     o  o o o o')
    print('    o    o  o     o  o')
    print('    o    o  o     o  o')
    print('    o    o  o o o o  o o o')
    print('    o    o  o     o  o')
    print('    o    o  o     o  o')
    print('     oooo   o     o  o o o o')
    print('')

  elif user_action.startswith('exit'):
    break

  else:
    print('Command is not valid!')

print('Thank you come again!')
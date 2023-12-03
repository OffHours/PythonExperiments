import re
import functions

completeCnt = 0

print('Your things to do are: ')
functions.listItems()

while True:
  user_action = input('Type add, show, edit, complete, clear, help or exit: ')
  user_action = user_action.strip() #Removes whitespace before and after the string

  if user_action.startswith('add'):
    todo = user_action[3:]

    functions.appItems(todo)

  elif  user_action.startswith('show'):
    functions.listItems()

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

      content  = functions.readLines()

      # Change the specific string
      content[int(changeNum)-1] = newTodo

      # Write the modified content back to the file
      functions.writeList(content)

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

      content  = functions.readLines()

        # Delete the specific item
      content.pop(completeNum-1)

      functions.writeList(content)

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

      content  = functions.readLines('todo.txt')

      # Delete the specific item
      content.pop(clearNum)

      # Write the modified content back to the file

      functions.writeList(content)

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

def listItems(mlPrint, filepath = 'todo.txt'):
  """list items in textfile, filepath should be the path to your txt file."""
  with open(filepath, 'r') as f:
      for lineNumber, lineContent in enumerate(f, start=1):
        mlPrint(f'{lineNumber} - {lineContent.strip()}')


def appItems(todo, filepath = 'todo.txt'): 
  """Append items to a textfile, filepath should be the path to your txt file."""
  with open(filepath, 'a') as f:
    f.write(f'{todo.strip()}\n')

def readLines(filepath = 'todo.txt'):
  """Read all lines in a text file and store return them as output"""
  with open(filepath, 'r') as f:
    y = f.readlines()
  return y

def writeList(y, filepath = 'todo.txt'):
  """Open txt file at the filepath provided as argument and store them in argument y"""
  with open(filepath, 'w') as f:
    for item in y:
      f.write(f'{item.strip()}\n')
      
def extractIndex(values,content):
  inner_list = values
  if inner_list:
      localTodo = inner_list[0].strip()  # Use the first element after stripping
      index = next((i for i, item in enumerate(content) if item.strip() == localTodo), None)
      
      return index

      #if index is not None:
         # print('todoVal:', todoVal)
        #  print('Index:', index)
     # else:
        #  print('Item not found in the list.')
  else:
    return 'No values in the list.'
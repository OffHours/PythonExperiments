
import PySimpleGUI as sg
import functions
"""
import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    event, values = sg.Window('My Script',
                    [[sg.Text('Document to open')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
"""

var = ['Big \n', 
       'Balls \n', 
       'of \n', 
       'fire \n' ]

completeCnt = 0


sg.theme('BluePurple')

col = [[sg.Button('Add', s = (7,None))],      
       [sg.Button('Edit', s = (7,None))],
       [sg.Button('Complete', s = (7,None))],
       [sg.Button('Clear', s = (7,None))]]           

layout = [[sg.Text('Your new todo: '), sg.Text(relief='sunken', size=(28,1) ,auto_size_text=False, key='-OUTPUT-')],
          [sg.Input(s = (47, None), tooltip = 'Enter a Todo', key='-TODO-', do_not_clear=True)],
          [sg.Listbox(values=[], size=(45, 10), key='-LIST-', enable_events=True), 
           sg.Column(col, vertical_alignment = 'top')],
          [sg.Button('Exit'), sg.Button('Help')]]


window = sg.Window('To-do app', layout, finalize = True)

window['-LIST-'].update(values=functions.readLines())

while True:  # Event Loop
    event, values = window.read()
    
    #print(event, values)
    
    if event == 'Add':
        
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-TODO-'])
        
        functions.appItems(values['-TODO-'])
        window['-LIST-'].update(values=functions.readLines())
    
    if event == 'Edit':
        #print(event, values)
        try:
            
            content = functions.readLines()
            
            index = content.index(values['-LIST-'][0])
            
            print(index)
            
            content[index] = values['-TODO-']

            # Write the modified content back to the file
            functions.writeList(content)
            window['-LIST-'].update(values=functions.readLines())

        except IndexError:
            print('Item is not in the list, try using the show command')
            continue
        
        except TypeError:
            print('¨You got a TypeError')
            continue
    
    if event == 'Complete':
        print(event, values)
        
        try:
            content = functions.readLines()
            print(content)
            index = content.index(values['-LIST-'][0])
            print(index)
            
            content.pop(index)

            # Write the modified content back to the file
            functions.writeList(content)
            window['-LIST-'].update(values=functions.readLines())
            
            completeCnt = completeCnt + 1
            window['-OUTPUT-'].update(f"You've completed {completeCnt} todos today!")
            
        except IndexError:
            print('Item is not in the list, try using the show command')
            continue
        except TypeError:
            print('You got a TypeError')
            continue
        
    if event == 'Clear':
        try:
            content = functions.readLines()
            #print(content)
            index = functions.extractIndex(values['-LIST-'], content)
            
            #print(index)
            
            
            window['-OUTPUT-'].update(f"You've cleared: {content[index]}")
            content.pop(index)
            
            # Write the modified content back to the file
            functions.writeList(content)
            window['-LIST-'].update(values=functions.readLines())
            
            
                
        except IndexError:
            print('Item is not in the list, try using the show command')
            continue
        except TypeError:
            print('You got a TypeError')
            continue
    
    if event == '-LIST-':
        
        print(values['-LIST-'][0])
        window['-TODO-'].update(value=values['-LIST-'][0])
        
    if event in ['Add', 'Edit', 'Complete', 'Clear']:
        print(event)
        window['-TODO-'].update(value='')
        
       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break


window.close()


import pandas as pd 
from fpdf import FPDF
from pathlib import Path
import glob

#Definiing several files in a common folder of type .xlsx using builtin glob function
filepaths = glob.glob('invoices/*xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    
    pdf = FPDF(orientation='P', unit = 'mm', format='A4')
    pdf.add_page()
    
    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=15, h=8,ln=1, txt=f'Invoice nr.{invoice_nr}')
    
    invoice_date = filename.split('-')[1]
    pdf.set_font(family='Times', size=12, style='')
    pdf.cell(w=0, h=8, align='L', txt=f'Date: {invoice_date}', ln=1)
    
    pdf.set_font(family='Helvetica', size=10, style='')
    pdf.set_fill_color(210, 210, 210)
    #pdf.set_text_color(100,100,100)
    
    col = list(df.columns)
    """
    #The below code does the same thing as the list() function above, because of... Reasons...
    for index, item in enumerate(df.columns):
        #print(index, item)
        col.append(item)
   """
   
    #Capitalize and replace underscores with space
    #col = [item.replace('_', ' ').title() for item in col]
    #This above does the same thing as below, also for reasons....
    #print(col, '\n')
    for index, text in enumerate(col):
        myString = text
        myString = myString.title()
        myString = myString.replace('_', ' ')
        col[index] = myString
    #print(col)
    
    #Add header
    pdf.cell(w=40, h=10, align='C', txt=col[0], border=1, fill=True)
    pdf.cell(w=50, h=10, align='C', txt=col[1], border=1, fill=True)
    pdf.cell(w=40, h=10, align='C', txt=col[2], border=1, fill=True)
    pdf.cell(w=30, h=10, align='C', txt=col[3], border=1, fill=True)
    pdf.cell(w=30, h=10, align='C', txt=col[4], ln=1, border=1, fill=True)
    

    #Add rows
    #totalAmount = 0
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=40, h=8, align='C', txt=str(row.iloc[0]), border=1)
        pdf.cell(w=50, h=8, align='C', txt=str(row.iloc[1]), border=1)
        pdf.cell(w=40, h=8, align='C', txt=str(row.iloc[2]), border=1)
        pdf.cell(w=30, h=8, align='C', txt=str(row.iloc[3]), border=1)
        pdf.cell(w=30, h=8, align='C', txt=str(row.iloc[4]), ln=1, border=1)
        
        #totalAmount = totalAmount + row.iloc[4]
        
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(80,80,80)
    pdf.cell(w=40, h=8, align='C', txt='', border=1)
    pdf.cell(w=50, h=8, align='C', txt='', border=1)
    pdf.cell(w=40, h=8, align='C', txt='', border=1)
    pdf.cell(w=30, h=8, align='C', txt='', border=1)
    pdf.cell(w=30, h=8, align='C', txt=str(df.iloc[:,4].sum()), ln=1, border=1) 
        
    pdf.ln(h = '')

    pdf.set_font(family='Times', size=12)
    pdf.cell(w=0, h=8, align='L', txt=f'Total amount due: {df.iloc[:,4].sum()}$', border=0, ln=1)
    
    pdf.ln(h = '')
    
    pdf.set_font(family='Times', size=10)
    #pdf.set_text_color(80,80,80)
    pdf.cell(w=0, h=8, align='L', txt='Lorem Ipsum Dolor Sit Amet', border=0, ln=1)
    pdf.set_font(family='Helvetica', size=12)
    pdf.cell(w=30, h=8, align='L', txt='Lorem Ipsum', ln=1)
    pdf.image('OH_LOGO_highres.png', x = None, y = None, w = 50, h = 0, type = 'PNG', link = '')
    
    pdf.output(f'PDFs/{filename}.pdf')

"""
#This code below takes converts the excel documents from filepaths into a list och pandas dataframe objects
#Then it concatenates the list of dataframes into a single dataframe and renumbers the index.

dfList = [] 
for index, filepath in enumerate(filepaths):
   
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    dfList.append(df)

df = pd.concat(dfList)

#print(df, '\n')

#index gets messed up when converting from list, this resets it counting from 1
df.reset_index(drop=True, inplace=True)

#print(df)
"""

import pandas as pd
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        #self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(0, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')



#Creating a PDF instance,P for portrait, lL for landscape
pdf = FPDF(orientation='p',unit='mm',format='A4')


#Creating a pandas dataframe object from a csv file
df = pd.read_csv('topics.csv')




for index, row in df.iterrows():
    
    #pdf = PDF()
    #pdf.alias_nb_pages()
    
    #Generating pages
    pdf.add_page()
    
    #PDF.header(pdf)
    #Setting font and cell content
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, 
            h=12,
            txt=row['Topic'],
            ln=1,
            border=0,
            align='L')
    pdf.line(10,21,200,21)
    
    for i in range(row['Pages']):
        
        pdf.add_page()
        
        
        
    #PDF.footer(pdf)



pdf.output('output.pdf')
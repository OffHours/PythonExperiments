import streamlit as st 
import plotly.express as px
import pandas as pd
import numpy as np
from backend import get_data

#Run this command to start the streamlit app
#streamlit run \Users\oscar\Documents\Python\pyenv1\weatherApp\Main.py
#When building a multipage app, for some reason the homepage, or main site, will be captalized or not based on 
#if the name of the .py file is capitalized when you run the start command and not the actual name on the file.


#Add title, text input, slider, select box and subheader
st.title('Weather Forecast')

place = st.text_input('Location: ')
days = st.slider('Forecast days', min_value=1, max_value=5,
                 help='Select the number of days for the forecast')

option = st.selectbox('Select data to view',
                      ('Temperature','Sky'))

st.subheader(f'{option} for the next {days} days in {place}')


if place:
    #Get temperature/sky-data from backend function
    filtered_data = get_data(place, days)


    #Visualize the data.
    if option == 'Temperature':
        temperature = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        #st.text(filtered_data)
        
        figure = px.line(x=dates, y=temperature , labels={'x':'Date', 'y':'Temperature(°C)'})
        st.plotly_chart(figure)


    if option == 'Sky':
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
  
        cols = []
        cols = st.columns(8) #= st.columns([3, 1]) the "3" and "1" sets teh width ratio
        num_columns = 8
        num_rows = len(sky_conditions) // num_columns

        times = []
        datesNew = []

        for index, item in enumerate(dates):
        
            dtt = item.split()
            dtt[0] = dtt[0].replace('-', '/')[5:]
            dtt[0] = '/'.join(reversed(dtt[0].split('/')))
            
            datesNew.append(dtt[0])
            times.append(dtt[1])
            #print(dates)
            #print(dtt[0])
            #print(dtt[1])
        
        for index in range(num_columns):
            text = times[index]
            text = text[:5]
            cols[index].text(text)

        for i in range(num_rows):
            for index in range(num_columns):
                #image = get_image_url(sky_conditions[index])
                image = f'images\{sky_conditions[index]}.png'
                text = datesNew[index]
                cols[index].image(image)
                cols[index].markdown(
                                    f"""
                                    <div style="display: flex; flex-direction: column; align-items: center;">
                                        <p>{text}</p>
                                    </div>
                                    """,
                                    unsafe_allow_html=True,
                                    )
                #cols[index].text(text)
                
            datesNew  = datesNew[8:]    
            sky_conditions = sky_conditions[8:]

#For debugging purposes
#st.session_state
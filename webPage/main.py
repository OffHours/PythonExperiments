from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    dfStations = pd.read_table('data-small\stations.txt', delimiter = ',', skiprows=17)
    
    dfView = dfStations[['STAID', 'STANAME                                 ', 'CN']]

    # Convert DataFrame to HTML
    table_html = dfView.to_html(classes='table table-bordered table-striped table-hover', index=False)

    # Render HTML template with the table
    return render_template('home.html', table_html=table_html)

@app.route('/api/v1/<station>/<date>')
def about(station, date): 
   
    filename = fr'data-small\TG_STAID{str(station).zfill(6)}.txt'

    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    dfStations = pd.read_table('data-small\stations.txt', delimiter = ',', skiprows=17)
    
    print(dfStations.columns)
    #Index(['STAID', 'STANAME                                 ', 'CN', '      LAT', '       LON', 'HGHT'], dtype='object')
    
    stationName = str(dfStations.loc[dfStations['STAID'] == int(station)]['STANAME                                 '].squeeze()).strip()
    temperature = (df.loc[df['    DATE'] == date]['   TG'].squeeze()) / 10
    
    
    return {"station": stationName,
            "date": date,
            "temperature": temperature}
    
    #"stationNr": station,
    #"df": str(df.loc[10, '   TG'])

@app.route('/api/v1/<station>')
def allData(station): 
    
    filename = fr'data-small\TG_STAID{str(station).zfill(6)}.txt'
    
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient='records')
    
    return result

@app.route('/api/v1/annual/<station>/<year>')
def year(station, year): 
    
    filename = fr'data-small\TG_STAID{str(station).zfill(6)}.txt'
    
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])


    # Filter the DataFrame for a specific year (e.g., 2022)
    dfYear = df[df['    DATE'].dt.year == int(year)]
    
    result = dfYear.to_dict(orient='records')
    
    return result

if __name__ == '__main__':
    app.run(debug=True)
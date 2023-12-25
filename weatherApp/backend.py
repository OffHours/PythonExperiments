import requests

API_KEY = 'INSERT YOUR API KEY HERE'

def get_data(place, days=None):
    
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric'
    
    #https://api.openweathermap.org/data/2.5/forecast?q=stockholm&appid='INSERT YOUR API KEY HERE'&units=metric
    
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    
    eon = days * 8
    
    filtered_data = filtered_data[:eon]
    
    """
    if option == 'Temperature':
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
        
    if option == 'Sky':
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]
        
    """
    return filtered_data

if __name__ == '__main__':
    #print(get_data(place='stockholm', days=5))
    ''
    
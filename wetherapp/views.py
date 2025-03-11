

from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = ''

def home(request):
    city = request.POST.get('city', 'Indore')  # Get city from POST, default to 'Indore'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    params = {'units': 'metric'}
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            temp = data['main']['temp']
            day = datetime.date.today()

            return render(request, 'index.html', {
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': day,
                'city': city,
            })
        else:
            messages.error(request, "City not found. Please enter a valid city name.")
    
    except requests.exceptions.RequestException:
        messages.error(request, "Failed to fetch weather data. Please try again later.")

    return render(request, 'index.html', {'city': city})

# from django.shortcuts import render
# import requests
# import datetime
# from django.contrib import messages
# def home(request):
#     if 'city' in request.POST:
#         city = request.POST['city']
#     else:
#         city = 'Indore'
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid='
#     PARAMS = {'units':'metric'}

#     API_KEY =  'AIzaSyCWISmywjFRw4HkxujVp49XIm35jQR2VAg'

#     SEARCH_ENGINE_ID = '739abe9ea725c40ee'
     
#     query = city + " 1920x1080"
#     page = 1
#     start = (page - 1) * 10 + 1
#     searchType = 'image'
#     city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

#     data = requests.get(city_url).json()
#     count = 1
#     search_items = data.get("items")
#     image_url = search_items[1]['link']
#     response = requests.get(url, params=PARAMS)
#     if response==200:
#         data = response.json()
#         description = data['weather'][0]['description']
#         icon = data['weather'][0]['icon']
#         temp = data['main']['temp']
#         day = datetime.date.today()
#         return render(request, 'index.html', {
#             'description': description,
#             'icon': icon,
#             'temp': temp,
#             'day': day,
#             'city': city,
#         })
#     except:
#         exception_occured=True
#         messages.error(request,'entered city is not available to api')
#         day=datetime.date.today()
#         return render(request, 'index.html', {
#             'description': 'clear sky',
#             'icon': '01d',
#             'temp': 25,
#             'day': day,
#             'city': 'indore',
#             'exception_occured':True
#         })

from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = '86deac85fe9e27625f6614cfe1c468c5'

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

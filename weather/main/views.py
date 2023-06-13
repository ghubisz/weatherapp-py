from django.shortcuts import render

import json

import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        #source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q ='
                +city +'&appid = 6eaf41e97d4f46a245bb5ebd32892267').read()

        #converting JSON data to a dictionary
        list_of_data = json.loads(source)

        #data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request, "main/index.html", data)

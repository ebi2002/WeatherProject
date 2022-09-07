import json
import requests as requests
city = input('the city name: ')
city.capitalize()
api_url_base = 'http://api.weatherapi.com/v1'
api_token = 'e817a0320e4243f5967123921220609'
url = f'http://api.weatherapi.com/v1/current.json?key=e817a0320e4243f5967123921220609&q={city}&aqi=no'
response = requests\
    .get(url)
print(response)

opening = requests.get(url)
print(opening.text)

y = json.dumps(opening.text)


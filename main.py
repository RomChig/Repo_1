import requests
KEY = 'ba89be5152a3f2584d8fc4de75381070'
URL='http://api.openweathermap.org/data/2.5/weather?q=London&appid='+KEY
resp = requests.get(URL)
a=resp.json()
print(a)
print()
print('Город: %s'%a['name'])
print('Погода: %s' %a['weather'][0]['description'])
print('Температура: %s'% a['main']['temp'])
print('Давление: %s'% a['main']['pressure'])
print('Влажность:%s '% a['main']['humidity'])
print('Видимость: %s'% a['visibility'])










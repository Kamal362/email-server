from pip._vendor import requests
responds = requests.get("https://goweather.herokuapp.com/weather/accra")
print(responds.json())
print("============================================")
data = responds.json()
print("the temperature in Accra is : ",data['temperature'])
print("the forcast for day 1 ", data['forecast'][0]['temperature'])
from pprint import pprint
import requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID={64cf3ae476e9d82677c0fb12030df926}')

pprint(r.json)
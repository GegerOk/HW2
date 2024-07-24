import requests
import pprint

r = requests.get ('https://gsgen.ru/gs-views/gsgen-ru/js/json-data/fish-text-parts.json.js')
print (r.text)
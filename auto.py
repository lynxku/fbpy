import requests
import bs4

res = requests.get('https://learncodeonline.in')
type(res)
res.text

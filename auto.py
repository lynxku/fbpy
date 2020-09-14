import requests
import bs4
import os
import sys

logo = ("Xzylus Remote Website")

os.system('clear')
print(logo)
print("Example : https://xzylus.com/shell.php")
url = input('Url >>> ')
res = requests.get(url)
type(res)
output = res.text
os.system('clear')
print(output)
soup = bs4.BeautifulSoup(res.text, 'lxml')
p = soup.select('title')
h1 = p[0].getText()
print("")
print("<<<=======Title=======>>>")
print(">>> " + h1 + " <<<")

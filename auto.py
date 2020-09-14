import requests
import bs4

print("Example : https://xzylus.com/shell.php")
url = input('Url >>>')
res = requests.get(url)
type(res)
output = res.text
print(output)

import requests
from bs4 import BeautifulSoup


url = "http://www.zeit.de/index"

url_content = requests.get(url)

output = BeautifulSoup(url_content.content, features="lxml")

print(output.prettify())

with open("lxml_test_scrap.xml", "w") as file:
    file.write(str(output))

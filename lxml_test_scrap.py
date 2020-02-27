from lxml import etree
import requests
from bs4 import BeautifulSoup
import urllib3

url = "http://www.zeit.de/index"

url_content = requests.get(url)

output = BeautifulSoup(url_content.content)

print(output.prettify())

with open("lxml_test_scrap", "w") as file:
    file.write(str(output))

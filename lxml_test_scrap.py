from lxml import html, etree
import requests

url = "https://www.zeit.de/index"

url_content = requests.get(url)

extracted_content = html.fromstring(url_content.content)


print(url_content.content)

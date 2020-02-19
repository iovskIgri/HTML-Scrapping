import requests
from lxml import html

page = requests.get("https://www.zeit.de/politik/ausland/2020-02/julian-assange-usa-donald-trump-begnadigung-russland")
tree = html.fromstring(page.content)

text = tree.xpath('//p[@class="paragraph article item"]/text()')

print(text)

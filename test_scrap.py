import requests
from lxml import html

page = requests.get("https://www.zeit.de/politik/ausland/2020-02/julian-assange-usa-donald-trump-begnadigung-russland")
tree = html.fromstring(page.content)

node_feat = '//p[@class="paragraph article__item"]/text()'
text = tree.xpath(node_feat)

print(text)

with open("paragraph article__item.txt","w") as file:
    for char in text:
        file.write(char)

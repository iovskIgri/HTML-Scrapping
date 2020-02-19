import requests
from lxml import html
#Anfrage an die Website
page = requests.get("https://www.zeit.de/politik/ausland/2020-02/julian-assange-usa-donald-trump-begnadigung-russland")
#Datentruktur speichert den Seiteninhalt
tree = html.fromstring(page.content)
#Name des gesuchten Features
node_feat = '//p[@class="paragraph article__item"]/text()'
#Isolierung des Featurenamens
name_split = node_feat.split('"')
filename = name_split[1]
#Seiteninhalt
text = tree.xpath(node_feat)
#Erstellung einer Datei und Speicherung des Texts
with open(filename + ".txt","w") as file:
    for char in text:
        file.write(char)

import requests
from lxml import html
#Anfrage an die Website
page = requests.get("https://www.zeit.de/index")

#Datentruktur speichert den Seiteninhalt
tree = html.fromstring(page.content)

#Name des gesuchten Features
node_feat_01 = '//p[@class="paragraph article__item"]/text()'
node_feat_02 = '//p[@class="zon-teaser-standard__text"]/text()'
node_feat_03 = '//span[@class="zon-teaser-standard__title"]/text()'
node_feat_04 = '//span[@class="zon-teaser-standard__kicker"]/text()'

#Isolierung des Featurenamens
name_split = node_feat_02.split('"')
filename = name_split[1]

#Seiteninhalt
texts = tree.xpath(node_feat_02)
titles = tree.xpath(node_feat_03)
kickers = tree.xpath(node_feat_04)
print(titles)
print (texts)
print(kickers)
#Erstellung einer Datei und Speicherung des Texts
with open(filename + ".txt","w") as file:
#    for headline in title:
#       file.write('{}{}{}'.format('Überschrift ', headline, '\n'))
#        file.write(char + "\n\n")

    for i in range(0,len(texts)-1):
        file.write('{}{}{}'.format('Kicker: ', kickers[i], '\n'))
        file.write('{}{}{}'.format('Überschrift: ', titles[i], '\n'))
        file.write('{}{}{}'.format('Artikel: ', texts[i], '\n'))
        file.write('\n\n')
        i+1


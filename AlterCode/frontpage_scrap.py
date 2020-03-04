import requests
from lxml import html
import time

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
print(texts)
print(kickers)


def get_date():
    # Aktuelle Uhrzeit
    localtime = time.asctime(time.localtime(time.time()))
    month = localtime[4] + localtime[5] + localtime[6]
    day = localtime[8] + localtime[9]
    hour = localtime[11] + localtime[12]
    minute = localtime[14] + localtime[15]
    year = localtime[20] + localtime[21] + localtime[22] + localtime[23]
    date = "{}_{}_{}_{}{}".format(year,month, day,hour, minute)

    return date


with open(get_date()+"_"+filename + ".txt","w") as file:
    for i in range(0,len(texts)-1):
        file.write('{}{}{}'.format('Kicker: ', kickers[i+1], '\n'))
        file.write('{}{}{}'.format('Überschrift: ', titles[i], '\n'))
        file.write('{}{}{}'.format('Artikel: ', texts[i], '\n'))
        file.write('\n\n')







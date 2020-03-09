import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import time

#Objekt durchsucht den HTML Baum.
parser = etree.HTMLParser()

#Baumobjekt das mit dem zuvor definierten Parser durchsucht werden kann.
tree = etree.parse("soup_test_scrap.xml", parser)

#Definitionen der gesuchten HTML Tags als Listen. Xpath-Ausdruck gibt den Text aller Baumknoten wieder, die das definierte Tag haben.
elements_text = tree.xpath('//p[@class="zon-teaser-standard__text"]/text()')
elements_title = tree.xpath('//span[@class="zon-teaser-standard__title"]/text()')

#Methode zur Ermittlung des Datums und der Uhrzeit des Scraps. Sie wird später bei der Erstellung des Dateinamens verwendet.
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

#Methode zum Auslesen des HTML Contents einer Webseite. Erwartet die zu scrapende URL als String.
def soup_scrap(url):
#    url = "http://www.zeit.de/index"

    url_content = requests.get(url)
    output = BeautifulSoup(url_content.content, features="lxml")

    with open(get_date() + "_" + "soup_scrap.xml", "w") as file:
        file.write(str(output))

    return file


def search_tree(filename):
    # Schreibe die Datei mit gegebenen Daten in gegebenes Format.
    with open(filename, "w+") as file:
        for i in range(0, len(elements_title) - 1):
            file.write("{}{}{}{}".format(elements_title[i], "\n", elements_text[i], "\n\n"))

    return file

import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import time


#Definition der beiden "Durchsuchungsobjekte" die ihre jeweilige Baumstruktur dursuchen werden.
#zeit.de
zon_parser = etree.HTMLParser()
#nzz.ch
nzzon_parser = etree.HTMLParser()


#Methode zur Ermittlung des Datums und der Uhrzeit des Scraps. Sie wird später bei der Erstellung des Dateinamens verwendet.
def get_date():
    # Aktuelle Uhrzeit
    localtime = time.asctime(time.localtime(time.time()))
    #Die Buchstaben des Monats stehen an Stelle 4, 5 und 6 in der Liste localtime.
    month = localtime[4] + localtime[5] + localtime[6]
    #Die Tageszahlen stehen an Stelle 8 und 9 in der Liste localtime.
    day = localtime[8] + localtime[9]
    #Die Stundezahlen stehen an Stelle 11 und 12 in der Liste localtime.
    hour = localtime[11] + localtime[12]
    #Die Minutenzahlen stehen an Stelle 14 und 15 in der Liste localtime.
    minute = localtime[14] + localtime[15]
    #Die Jahreszahlen steht an Stelle 20, 21, 22 und 23 in der Liste localtime.
    year = localtime[20] + localtime[21] + localtime[22] + localtime[23]
    date = "{}_{}_{}_{}{}".format(year,month, day,hour, minute)

    return date

#Definition der Dateinamen, die sich aus dem aktuellen Datum und der Uhrzeit ergeben.
zon_filestring = get_date() + "_" + "zon_soup_scrap.xml"
nzzon_filestring = get_date() + "_" + "nzzon_soup_scrap.xml"

#Methode zum Schreiben des HTML Contents einer Webseite in eine xml Datei. Erwartet die zu scrapende URL als String.
#Das Speichern ist notwendig da sonst nicht gezielt auf Tags zurückgegriffen werden kann, es kommt zu einem Synchronisationsfehler.
def soup_scrap(url):

    #Definition der Abfrage des Web-Inhalts
    url_content = requests.get(url)
    #Definition der Ausgabe des von BeatifulSoup4 bereitgestellten Web-Inhalts
    output = BeautifulSoup(url_content.content, features="lxml")

    #Festlegen welcher Dateiname, in Abhängigkeit von der gecrappten Seite, gewählt werden soll.
    if (url == "https://www.zeit.de/index"):

        with open(zon_filestring, "w") as file:
            file.write(str(output))
        return file

    else:

        with open(nzzon_filestring, "w") as file:
            file.write(str(output))
        return file

#Methode zur Überprüfung der Formatierung der gescrappten Daten. Sie dient lediglich zum Debugging von Formatfehlern.
def search_tree(filename):
    # Schreibe die Datei mit gegebenen Daten in gegebenes Format.
    with open(filename, "w+") as file:
        for i in range(0, len(zon_elem_title) - 1):
            file.write("{}{}{}{}".format(zon_elem_title[i], "\n", zon_elem_text[i], "\n\n"))

    return file


#Auslösen des jeweiligen Scraps.
soup_scrap('https://www.zeit.de/index')
soup_scrap('https://www.nzz.ch')

#Definition des jeweiligen Baumobjekts und Zuweisung des zugehörigen Durchsuchungsobjekts.
zon_tree = etree.parse(zon_filestring, zon_parser)
nzzon_tree = etree.parse(nzzon_filestring, nzzon_parser)


#Definitionen der gesuchten HTML Tags als Listen. Xpath-Ausdruck gibt den Text aller Baumknoten wieder, die das definierte Tag haben.
#zeit.de
zon_elem_text = zon_tree.xpath('//p[@class="zon-teaser-standard__text"]/text()')
zon_elem_title = zon_tree.xpath('//span[@class="zon-teaser-standard__title"]/text()')
zon_elem_author = zon_tree.xpath('//span[@class="zon-teaser-standard__byline"]/text()')
#nzz.ch
nzzon_elem_text = nzzon_tree.xpath('//div[@class="teaser__lead teaser__lead--2of3 teaser__lead--longformstandard"]/text()')
nzzon_elem_title = nzzon_tree.xpath('//span[@class="teaser__title-name"]/text()')
nzzon_elem_author = nzzon_tree.xpath('//span[@class="metainfo__item metainfo__item--author"]/text()')


#Alles hier drunter ist zum Debugging da.
print(nzzon_elem_title)
print(nzzon_elem_text)
print(nzzon_elem_author)

print(zon_elem_title)
print(zon_elem_text)
print(zon_elem_author)

#search_tree(spon_filestring)
#search_tree(zon_filestring)
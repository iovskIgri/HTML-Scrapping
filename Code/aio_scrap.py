import requests
from bs4 import BeautifulSoup
from lxml import html, etree
import pymysql.cursors
import time

# Definition der beiden "Durchsuchungsobjekte" die ihre jeweilige Baumstruktur dursuchen werden.
# TODO niedriger Prio: Zuweisung des Parsers als allgemeine Methode.

# zeit.de
zon_parser = etree.HTMLParser()

# nzz.ch
nzzon_parser = etree.HTMLParser()

# hon.com
hon_parser = etree.HTMLParser()

# tagon.de
tagon_parser = etree.HTMLParser()

# dwon.com
dwon_parser = etree.HTMLParser()


# Methode zur Ermittlung des Datums und der Uhrzeit des Scraps. Sie wird später bei der Erstellung des Dateinamens
# verwendet.

def get_date():

    # Aktuelle Uhrzeit
    localtime = time.asctime(time.localtime(time.time()))
    # Die Buchstaben des Monats stehen an Stelle 4, 5 und 6 in der Liste localtime.
    month = localtime[4] + localtime[5] + localtime[6]
    # Die Tageszahlen stehen an Stelle 8 und 9 in der Liste localtime.
    day = localtime[8] + localtime[9]
    # Die Stundezahlen stehen an Stelle 11 und 12 in der Liste localtime.
    hour = localtime[11] + localtime[12]
    # Die Minutenzahlen stehen an Stelle 14 und 15 in der Liste localtime.
    minute = localtime[14] + localtime[15]
    # Die Jahreszahlen steht an Stelle 20, 21, 22 und 23 in der Liste localtime.
    year = localtime[20] + localtime[21] + localtime[22] + localtime[23]
    date = "{}_{}_{}_{}{}".format(year, month, day, hour, minute)

    return date


# Definition der Dateinamen, die sich aus dem aktuellen Datum und der Uhrzeit ergeben.
# TODO niedriger Prio: Filestring Objekt Erstellung per allgemeingültiger Methode.

zon_filestring = get_date() + "_" + "zon_soup_scrap.xml"
nzzon_filestring = get_date() + "_" + "nzzon_soup_scrap.xml"
hon_filestring = get_date() + "_" + "hon_soup_scrap.xml"
tagon_filestring = get_date() + "_" + "tagon_soup_scrap.xml"
dwon_filestring = get_date() + "_" + "dwon_soupscrap.xml"


# Methode zum Schreiben des HTML Contents einer Webseite in eine xml Datei. Erwartet die zu scrapende URL als String.
# Das Speichern ist notwendig da sonst nicht gezielt auf Tags zurückgegriffen werden kann, es kommt zu einem
# Synchronisationsfehler.

def soup_scrap(url):

    # Definition der Abfrage des Web-Inhalts
    url_content = requests.get(url)

    # Definition der Ausgabe des von BeatifulSoup4 bereitgestellten Web-Inhalts.
    site_content = BeautifulSoup(url_content.content, features="lxml")
    output = site_content

    # Festlegen welcher Dateiname, in Abhängigkeit von der gecrappten Seite, gewählt werden soll.
    if url == "https://www.zeit.de/index":
        with open(zon_filestring, "w") as file:
            file.write(str(output))
        return file

    if url == "https://www.handelsblatt.com":
        with open(hon_filestring, "w") as file:
            file.write(str(output))
        return file

    if url == "https://www.tagesschau.de":
        with open(tagon_filestring, "w") as file:
            file.write(str(output))
        return file

    if url == "https://www.dw.com/de/top-stories/s-9077":
        with open(dwon_filestring, "w") as file:
            file.write(str(output))
        return file
    else:

        with open(nzzon_filestring, "w") as file:
            file.write(str(output))
        return file


# Auslösen des jeweiligen Scraps.

soup_scrap('https://www.zeit.de/index')
soup_scrap('https://www.nzz.ch')
soup_scrap('https://www.handelsblatt.com')
soup_scrap('https://www.tagesschau.de')
soup_scrap('https://www.dw.com/de/top-stories/s-9077')

# Definition des jeweiligen Baumobjekts und Zuweisung des zugehörigen Durchsuchungsobjekts.
# TODO niedriger Prio: Baumobjekterstellung und Parserzuweisung per Methode.

zon_tree = etree.parse(zon_filestring, zon_parser)
nzzon_tree = etree.parse(nzzon_filestring, nzzon_parser)
hon_tree = etree.parse(hon_filestring, hon_parser)
tagon_tree = etree.parse(tagon_filestring, tagon_parser)
dwon_tree = etree.parse(dwon_filestring, dwon_parser)

# Xpath-Ausdruck gibt den Text aller Baumknoten wieder, die das definierte Tag haben. Das durch das Tag
# wiedergegebene Element ist ein String, der in der Elementliste (xxx_elem_xxx) gespeichert wird.
# TODO niedriger
#  Prio: Beiseitigung von Indexfehlern, die durch verschiedene Atikelstrukturen der Webseiten erzeugt werden. DIES
#  SIND DIE IN DIE DATENBANK ZU SCHREIBENDEN VARIABLEN zeit.de (database ready)

zon_elem_text = zon_tree.xpath('//p[@class="zon-teaser-standard__text"]/text()')
zon_elem_title = zon_tree.xpath('//span[@class="zon-teaser-standard__title"]/text()')
zon_elem_author = zon_tree.xpath('//span[@class="zon-teaser-standard__byline"]/text()')
zon_list = [zon_elem_title, zon_elem_text, zon_elem_author, 'Zeit']

# nzz.ch(database ready)
nzzon_elem_text = nzzon_tree.xpath(
    '//div[@class="teaser__lead teaser__lead--2of3 teaser__lead--longformstandard"]/text()')
nzzon_elem_title = nzzon_tree.xpath('//span[@class="teaser__title-name"]/text()')
nzzon_elem_author = nzzon_tree.xpath('//span[@class="metainfo__item metainfo__item--author"]/text()')
nzzon_list = [nzzon_elem_title, nzzon_elem_text, nzzon_elem_author, 'Neu Zuericher Zeitung']

# hon.com(database ready)
hon_elem_text = hon_tree.xpath('//p[@class="vhb-teaser-content"]/text()')
hon_elem_title = hon_tree.xpath('//span[@class="vhb-headline"]/text()')
hon_elem_author = hon_tree.xpath('//span[@class="vhb-author"]/text()')
hon_list = [hon_elem_title, hon_elem_text, hon_elem_author, 'Handelsblatt']

# tagesschau.de(database ready)
tagon_elem_text = tagon_tree.xpath('//p[@class="teasertext"]/text()')
tagon_elem_title = tagon_tree.xpath('//h4[@class="headline"]/text()')
tagon_elem_author = tagon_tree.xpath('//em')
tagon_list = [tagon_elem_title, tagon_elem_text, tagon_elem_author, 'Tagesschau']


# TODO HOHER PRIO: Einlesen der Strings, die in den Elementlisten (xxx_elem_xxx) enthalten sind, in die Datenbank.

# Methode zum Einlesen von Elementen in die MySQL Datenbank.
# @param list: Liste von Strings zu bestimmten Scraps, enthält vier Elemente.

def write_to_database(list):

    # Definition der Parameter für die Verbindug mit dem Host der Datenbank.
    connection = pymysql.connect(host='localhost', user='root', password='', database='html_scrapping',
                                 charset='utf8mb4')

    # Das Schreiben der Daten wird in einem try und finally Block abgewickelt damit Exceptions abgefangen werden können.
    # Außerdem kann damit ein Schließen der Verbindung sicher gestellt werden.
    try:

        with connection.cursor() as cursor:

            # Definition der von pymySQL genutzten Expressions um die Datenbank zu befüllen
            # als Variable zur besseren Leserlichkeit.
            author = "INSERT INTO autor(name) VALUES(%s)"
            article = "INSERT INTO artikel(schlagzeile, artikeltext) VALUES(%s, %s)"
            source = "INSERT INTO quelle(bezeichnung) VALUES(%s)"
            scrap_time = "INSERT INTO datum(einlesezeitpunkt) VALUES(%s)"

            # Zuweisen der Änderungen der Datenbank.
            cursor.execute(author, list[2])
            cursor.execute(article, list[0], list[1])
            cursor.execute(source, list[3])
            cursor.execute(scrap_time, get_date())

        # Bestätigung der zugewiesenen Änderungen
        connection.commit()

    # Schließen der Verbindung
    finally:
        connection.close()


# dwon.com (Hier muss ich mir noch eine bessere Verarbeitung der gescrapten Daten überlegen. Vorerst auslassen)
dwon_elem_text = dwon_tree.xpath('//p/text()')


# dwon_elem_title = dwon_tree.cpath('//h4/text()')


# HILFSMETHODEN.

# Methode zur Überprüfung der Formatierung der gescrappten Daten. Sie dient lediglich zum Debugging von Formatfehlern.

def search_tree(filename):

    # Schreibe die Datei mit gegebenen Daten in gegebenes Format.
    with open(filename, "w+") as file:
        for i in range(0, len(zon_elem_title) - 1):
            file.write("{}{}{}{}".format(zon_elem_title[i], "\n", zon_elem_text[i], "\n\n"))

    return file

# Kommentar entfernen um sich Elementliste anzeigen zu lassen.
# print(nzzon_elem_title)
# print(nzzon_elem_text)
# print(nzzon_elem_author)

# print(zon_elem_title)
# print(zon_elem_text)
# print(zon_elem_author)

# print(hon_elem_title)
# print(hon_elem_text)
# print(hon_elem_author)

# print(dwon_elem_text)

# print(tagon_elem_title)
# print(tagon_elem_text)
# print(tagon_elem_author)

# search_tree(spon_filestring)
# search_tree(zon_filestring)

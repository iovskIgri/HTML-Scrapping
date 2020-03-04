from lxml import html, etree
#Objekt durchsucht den HTML Baum.
parser = etree.HTMLParser()
#Baumobjekt das mit dem zuvor definierten Parser durchsucht werden kann.
tree = etree.parse("lxml_test_scrap.xml", parser)

#Definitionen der gesuchten HTML Tags als Listen. Xpath-Ausdruck gibt den Text aller Baumknoten wieder, die das definierte Tag haben.
elements_text = tree.xpath('//p[@class="zon-teaser-standard__text"]/text()')
elements_title = tree.xpath('//span[@class="zon-teaser-standard__title"]/text()')


#Schreibe die Datei mit gegebenen Daten in gegebenes Format.
with open("articles.txt","w+") as file:
    for i in range(0, len(elements_title)-1):
        file.write("{}{}{}{}".format(elements_title[i], "\n", elements_text[i], "\n\n"))

#print(elements_article)
print(len(elements_title))
print(len(elements_text))

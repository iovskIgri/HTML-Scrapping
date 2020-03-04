from lxml import html, etree

parser = etree.HTMLParser()

tree = etree.parse("lxml_test_scrap.xml", parser)

root = tree.getroot()

elements_text = tree.xpath('//p[@class="zon-teaser-standard__text"]/text()')
elements_title = tree.xpath('//span[@class="zon-teaser-standard__title"]/text()')
elements_kicker = tree.xpath('//span[@class="zon-teaser-standard__kicker"]/text()')
elements_article = list()

for i in range(0, len(elements_title)-1):
    for i in range(0,len(elements_text)-1):
        elements_article.append(elements_title[i])
        elements_article.append(elements_text[i])

'{}{}{}{}'.format()

#print(elements_kicker[1])
#print(elements_title[1])
#print(elements_text[1])

#print(elements_article)
print(len(elements_title))
print(len(elements_text))
print(len(elements_article))
print(elements_article)

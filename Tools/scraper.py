from lxml import html
import requests


#page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get('https://thepiratebay.org/search/python/0/99/0')
tree = html.fromstring(page.content)

#This will create a list of buyers:
#buyers = tree.xpath('//li[@class="result-row"]/text()')
name = tree.xpath('//a[@class="detLink"]/text()')
#This will create a list of prices
uploaded = tree.xpath('//font[@class="detDesc"]/text()')

print('Name: ', name)
print ('Uploaded: ', uploaded)
#





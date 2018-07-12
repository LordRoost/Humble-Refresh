from lxml import html
import requests

page = requests.get('https://www.humblebundle.com/books/star-trek-magazine-bundle')
tree = html.fromstring(page.content)
average = tree.xpath('/html/body/div/div[2]/div[4]/div[1]/div[2]/div[3]/div/div/text()')
#average = tree.xpath('//div/div[2]/div[4]/div[1]/div[2]/div[3]/div/div/text()')
#page.content
#page.text
#print ("Average: ", average)
print(average)

s = average[0]
l = []
for t in s.split():
	try:
		l.append(float(t))
	except ValueError:
		pass
		
print(l)
from lxml import html
import requests

page = requests.get('https://www.humblebundle.com')
tree = html.fromstring(page.content)
average = tree.xpath('/html/body/div/div[2]/div[4]/div[1]/div[2]/div[3]/div/div/text()')

print average
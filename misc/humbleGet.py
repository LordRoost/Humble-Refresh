from bs4 import BeautifulSoup
import requests
import re

page = requests.get('https://www.humblebundle.com/')
c = page.content
soup = BeautifulSoup(c, "lxml")
samples = soup.find_all(class_="prepend section-heading price bta ")
avg = str(samples[0]) # str needed because its a soup object

p = re.findall( r'\d+\.*\d*', avg) #using regex finds float numbers

price = p[0]
print(price)

fo = open("avg.txt", "r+")
fo.seek(0,0)
line = fo.write(price)


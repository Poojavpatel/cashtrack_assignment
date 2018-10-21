import urllib.request
from bs4 import BeautifulSoup
import csv
f = open('dataoutput.csv', 'w', newline = '')
writer = csv.writer(f)

myurl = "https://ada.com/conditions/"
soup = BeautifulSoup(urllib.request.urlopen(myurl), 'html.parser')

links = soup.find_all('a', attrs={"class":"s1lrc7ah-2"})
linkslist = [p for p in links]
# print(linkslist)
print(len(alllinkslist))
for foo in linkslist

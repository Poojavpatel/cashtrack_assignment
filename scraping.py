import urllib.request
from bs4 import BeautifulSoup
import csv
f = open('dataoutput.csv', 'w', newline = '')
writer = csv.writer(f)

myurl = "https://ada.com/conditions/"
soup = BeautifulSoup(urllib.request.urlopen(myurl), 'html.parser')

links = soup.find_all('a', attrs={"class":"s1lrc7ah-2"})
links = [p for p in links]

for foo in links: 
    col = [foo.text.strip(), foo["href"]]
    print(col)
# foo = linkslist[0]
# print("name:")
# print(foo.text.strip())
# print("link:")
# print(foo["href"])
# print(linkslist)
# print(len(linkslist))
# for i in linkslist:
#     print(i)

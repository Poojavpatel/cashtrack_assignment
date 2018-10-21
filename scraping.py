import urllib.request
from bs4 import BeautifulSoup
import csv
f = open('dataoutput.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['name','link'])

soup = BeautifulSoup(urllib.request.urlopen("https://ada.com/conditions/"), 'html.parser')

links = soup.find_all('a', attrs={"class":"s1lrc7ah-2"})
links = [p for p in links]

for foo in links: 
    col = [foo.text.strip(), foo["href"]]
    writer.writerow(col)
    print(col)

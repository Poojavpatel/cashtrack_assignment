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
    link=foo["href"]
    col = [foo.text.strip(), link]
    writer.writerow(col)
    # print(col)
    soup2 = BeautifulSoup(urllib.request.urlopen(link), 'html.parser')
    inner = soup2.find('ol',attrs={"class":"s13vxsj7-0"}).findChildren('li')
    inner = [p for p in inner]
    print(inner)

# <ol class="s13vxsj7-0 iUCILt" id="contents"><li><a href="#what-is-achilles-tendonitis">What is Achilles tendonitis?</a></li><li><a href="#symptoms">Symptoms</a></li><li><a href="#causes">Causes</a></li><li><a href="#diagnosis">Diagnosis</a></li><li><a href="#treatment">Treatment</a></li><li><a href="#prevention">Prevention</a></li><li><a href="#faq">FAQ</a></li><li><a href="#other-ways-to-refer-to-achilles-tendonitis">Other ways to refer to Achilles tendonitis</a></li></ol>
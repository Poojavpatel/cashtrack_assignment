import urllib.request, csv
from bs4 import BeautifulSoup

f = open('dataoutput.csv', 'w', newline = '')
writer = csv.writer(f)
writer.writerow(['name','link','What is?','Symptoms','Causes','Diagnosis','Treatment', 'Prevention'])

soup = BeautifulSoup(urllib.request.urlopen("https://ada.com/conditions/"), 'html.parser')

links = soup.find_all('a', attrs={"class":"s1lrc7ah-2"})
links = [p for p in links]

for foo in links:
    link=foo["href"]
    # col = [foo.text.strip(), link]
    # writer.writerow(col)
    soup2 = BeautifulSoup(urllib.request.urlopen(link), 'html.parser')
    sibs = soup2.find(attrs={"id":"symptoms"}).next_siblings
    sibs2 = [sib.text.strip() for sib in sibs if sib != '\n']
    print(sibs2)
    # for sib in sibs:
    #     if(sib.name != 'h2'):
    #         # s1.append(sib.strip())
    #         print(sib)
    #     else:
    #         break

# for p in list:
#     foo = p.findChildren('a')
#     print(foo)
# list = soup.find('ul', attrs={'class':'s1lrc7ah-1 kltjHF'}).findChildren('li')
# print(type(list))
# print(type(list[0]))
# listb = list[0].findChildren('a')
# .findChildren('a', attrs={'class':'s1lrc7ah-2'})
# list = [ele.text.strip() for ele in list] 
# print(listb)
# writer.writerow(tbody)

# foo = linkslist[0]
# print("name:")
# print(foo.text.strip())
# print("link:")
# print(foo["href"])
# print(linkslist)
# print(len(linkslist))
# for i in linkslist:
#     print(i)

# soup2 = BeautifulSoup(urllib.request.urlopen(link), 'html.parser')
#     inner = soup2.find('ol',attrs={"class":"s13vxsj7-0"})
#     print(inner)

# inner = [<li><a href="#what-is-achilles-tendonitis">What is Achilles tendonitis?</a></li>, <li><a href="#symptoms">Symptoms</a></li>, <li><a href="#causes">Causes</a></li>, <li><a href="#diagnosis">Diagnosis</a></li>, <li><a href="#treatment">Treatment</a></li>, <li><a href="#prevention">Prevention</a></li>, <li><a href="#faq">FAQ</a></li>, <li><a href="#other-ways-to-refer-to-achilles-tendonitis">Other ways to refer to Achilles tendonitis</a></li>]

# .findChildren a = [[<a href="#what-is-achilles-tendonitis">What is Achilles tendonitis?</a>], [<a href="#symptoms">Symptoms</a>], [<a href="#causes">Causes</a>], [<a href="#diagnosis">Diagnosis</a>], [<a href="#treatment">Treatment</a>], [<a href="#prevention">Prevention</a>], [<a href="#faq">FAQ</a>], [<a href="#other-ways-to-refer-to-achilles-tendonitis">Other ways to refer to Achilles tendonitis</a>]]

# .find all = [<bound method Tag.find_all of <li><a href="#what-is-achilles-tendonitis">What is Achilles tendonitis?</a></li>>, <bound method Tag.find_all of <li><a href="#symptoms">Symptoms</a></li>>, <bound method Tag.find_all of <li><a href="#causes">Causes</a></li>>, <bound method Tag.find_all of <li><a href="#diagnosis">Diagnosis</a></li>>, <bound method Tag.find_all of <li><a href="#treatment">Treatment</a></li>>, <bound method Tag.find_all of <li><a href="#prevention">Prevention</a></li>>, <bound method Tag.find_all of <li><a href="#faq">FAQ</a></li>>, <bound method Tag.find_all of <li><a href="#other-ways-to-refer-to-achilles-tendonitis">Other ways to refer to Achilles tendonitis</a></li>>]

# strip = ['What is Achilles tendonitis?', 'Symptoms', 'Causes', 'Diagnosis', 'Treatment', 'Prevention', 'FAQ', 'Other ways to refer to Achilles tendonitis']

# ['What is acne vulgaris?', 'Causes', 'Symptoms', 'Diagnosis', 'Treatment', 'FAQ', 'Other names for acne vulgaris']

# inner = soup2.find('ol',attrs={"class":"s13vxsj7-0"}).findChildren('li')
    # inner = [p.findChildren('a') for p in inner]
    # # print(inner)
    # # col = [foo.text.strip(), link, ]
    # for biz in inner:
    #     s = 

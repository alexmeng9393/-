 import requests
from bs4 import BeautifulSoup
url='https://jgirl.ddns.net/WebPages/%E9%95%B7%E6%81%A8%E6%AD%8C.htm'
WebPage=requests.get(url)
soup = BeautifulSoup(WebPage.text,'html5lib')
divs = soup.find_all(class_ ='MsoNormal')
s1 = ''
for i in divs:
s1 += i.text
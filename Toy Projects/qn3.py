from bs4 import BeautifulSoup
import requests



url="https://www.boxofficemojo.com/"
page=requests.get(url)
soup=BeautifulSoup(page.content, 'html.parser')

# doc = lh.fromstring(page.content)

tables = soup.find('table', id='hp_boxoffice')
movies=list()
collection = dict()



for row in tables.find_all("td"):
   movies.append(row)


for each in movies:
    print(each.text)

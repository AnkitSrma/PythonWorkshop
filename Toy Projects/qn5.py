from bs4 import BeautifulSoup
import requests



url="https://techlekh.com/"
page=requests.get(url)
soup=BeautifulSoup(page.content, 'html.parser')

# doc = lh.fromstring(page.content)

links = soup.find_all('a')

f = open("links.txt", "a")

for each in links:
    f.write(each.text + "\n")
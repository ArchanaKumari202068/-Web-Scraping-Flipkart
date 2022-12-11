import requests
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DMi"

page = requests.get(url)

# print(page.content)

soup = BeautifulSoup(page.content,"html.parser")

phones = soup.find_all("div",class_="_1AtVbE")

links = []

phones_names = []

for phone in phones:
    name = phone.find_all('div',class_="_4rR01T");
    for x in name:
        print(x.text)
    lks = phone.find_all('a',class_="_1fQZEK")

    for y in lks:
        print('https://www.flipkart.com'+y['href'])

# print(phones)
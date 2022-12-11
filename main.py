
# https://www.flipkart.com/xiaomi-11i-5g-stealth-black-128-gb/p/itmf5300d828d19f?pid=MOBG9QXPQ2F8KGQD&lid=LSTMOBG9QXPQ2F8KGQDBEHA2F&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_1&otracker=CLP_Filters&fm=organic&iid=5ede2f15-50c6-47f2-bdb0-22ff4759ec74.MOBG9QXPQ2F8KGQD.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=4bw7mm2k740000001670681244072
import requests
from bs4 import BeautifulSoup
import pandas as pd
url ="https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DMi"

req = requests.get(url)
content = BeautifulSoup(req.content,'html.parser')
# print (content)

data = content.find_all('div',{'class':"_2kHMtA"})
# print(data)

links = []
phn_name = []
start_link = "https://www.flipkart.com"
for items in data:
        rest_link= items.find('a')['href']
        name =items.find('div',class_='_4rR01T')
        links.append(start_link+rest_link)
        phn_name.append(name.string)
        # print(rest_link)
        # print((name.string))
# print(links)
# print(phn_name[0])
# print(links[0])  


dataframes={'phone_names':phn_name,'Links':links}
final_dataframes =pd.DataFrame(dataframes)
# print(final_dataframes)

final_dataframes.to_csv("web_scraping_flipkart.csv")






# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# url = "https://www.flipkart.com/search?sid=tyy%2C4io&otracker=CLP_Filters&p%5B%5D=facets.brand%255B%255D%3DMi"
# send request
# r = requests.get(url)
# print(r)
# soup = BeautifulSoup(r.text, "lxml")
# access the data
# soup = BeautifulSoup(r.text, "lxml")
# print(soup)
# # np = next page


# for a in soup.find_all('a', class_="_1LKTO3"):
#     print("Found the URL:", a['href']) 
# while True:




# np = soup.find("a",class_="_1fQZEK").get('href')
# print(np)

# for a in soup.find_all('a', class_="_1fQZEK"  ):
#     print("Found the URL:", a['href']) 

# cnp = "https://www.flipkart.com"+np


# print(cnp)

    # url =cnp
    # r= requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")

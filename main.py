import requests
from bs4 import BeautifulSoup


url="https://www.doviz.com/"

response=requests.get(url)
çorba=BeautifulSoup(response.text,"html.parser")

name=çorba.find_all("span",{"class":"name"})
value=çorba.find_all("span",{"class":"value"})
for isim,değer in zip(name,value):
    print(isim.text)
    print(değer.text)
    print("*************")
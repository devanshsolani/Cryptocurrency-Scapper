from bs4 import BeautifulSoup
import requests

URL="https://www.google.com/search?q="
QUERY1 = "bitcoin+prce+in+usd"
QUERY2 = "etherium+price+in+usd"
QUERY3 = "litecoin+price+in+usd"
def scrape1():
    r=requests.get(URL+QUERY1)
    s=BeautifulSoup(r.text,'html.parser')
    ans1=s.find("div",class_="BNeawe iBp4i AP7Wnd")
    return ans1.text

def scrape2():
    r=requests.get(URL+QUERY2)
    s=BeautifulSoup(r.text,'html.parser')
    ans2=s.find("div",class_="BNeawe iBp4i AP7Wnd")
    return ans2.text

def scrape3():
    r=requests.get(URL+QUERY3)
    s=BeautifulSoup(r.text,'html.parser')
    ans3=s.find("div",class_="BNeawe iBp4i AP7Wnd")
    return ans3.text
price1=scrape1()
price2=scrape2()
price3=scrape3()
print("Bitcoin: "+price1)
print("Etherium: "+price2)
print("Litecoin: "+price3)
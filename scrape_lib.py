import requests
from bs4 import BeautifulSoup
import datetime
import time
import smtplib, ssl

port = 465
password = input("Type your password: ")

context = ssl.create_default_context()

def extract_url(url):
    if url.find("www.amazon.co.uk") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.co.uk"+url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https//www.amazon.co.uk"+url[index:index2]
            else:
                url = None
    else:
        url = None
    return url


def get_converted_price(price):
    stripped_price = (float(price.strip("£")))
    return stripped_price

# this is my 'user agent'
def get_product_details(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    details = {"name": "", "price": 0, "deal": True, "url": ""}
    _url = extract_url(url)
    #print(_url)
    if _url is None:
        details = None
    else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        title = soup.find(id = "productTitle")
        price = soup.find(id="priceblock_dealprice")

        if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False

        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
            details["name"] = title.get_text().strip()
        else:
            details = None
        return details

#test = (get_product_details(url_list[0]))
#print(test)

def email(message):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
        server.login("drbencpython@gmail.com", password)
        server.sendmail("drbencpython@gmail.com", "coulsonba@gmail.com", str(message))
        print("Cheap price detected, email sent")

def add_prices(url_list):
    price_list = [[], [], [], [], [], [], [], [], [], [], []]
    timestamp = datetime.datetime.now()
    price_list[0].append(timestamp)
    for n, url_l in enumerate(url_list):
        url_l_r = (get_product_details(url_l))
        url_l_price = url_l_r["price"]
        price_list[n+1].append(url_l_price)

    prices = [float(str(n).replace("[", "]").replace("]", "")) for n in price_list[1:]]
    print("Prices are as follows: ")
    print(prices)

    #set email price thresholds here
    if int(prices[0]) < 10:
        email("cheap 71708")
    elif float(prices[1]) < 18:
        email("cheap gamers market")
    elif float(prices[2]) < 18:
        email("cheap car")
    elif float(prices[3]) < 15:
        email("cheap racers")
    elif float(prices[4]) < 27:
        email("cheap dragon")
    elif float(prices[5]) < 30:
        email("cheap mandalorian walker")
    elif float(prices[6]) < 12:
        email("cheap welcome to hidden side")
    elif float(prices[7]) < 7:
        email("cheap kai pod")
    elif float(prices[8]) < 7:
        email("cheap lloyd pod")
    elif float(prices[9]) < 7:
        email("cheap jay pod")

    return price_list

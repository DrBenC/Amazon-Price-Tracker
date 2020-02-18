import requests
from bs4 import BeautifulSoup
import datetime
import time
import smtplib, ssl
import scrape_lib as scl

## Dashboard

url_list = ["https://www.amazon.co.uk/LEGO-71707-LEGO-71707-NINJAGO-Kais-Mech-Jet-Plane-2-in-1-Building-Set-Prime-Empire-Racing-Series/dp/B07W6Q952Z/ref=sr_1_19?keywords=lego+ninjago&qid=1580830376&sr=8-19",
            "https://www.amazon.co.uk/LEGO-71708-LEGO-71708-NINJAGO-Gamers-Market-Nine-Minifigures-Set-with-Digi-Jay-Avatar-Pink-Zane-and-Avatar-Harumi/dp/B07W5PXWMD/ref=sr_1_24?keywords=lego+ninjago&qid=1580830376&sr=8-24",
            "https://www.amazon.co.uk/LEGO-71710-LEGO-71710-Ninjago-Ninja-Tuner-Car-with-Spreading-Blades-Building-Set-Prime-Empire-Racing-Vehicles/dp/B07W8XYZ2K/ref=sr_1_30?keywords=lego+ninjago&qid=1580830376&sr=8-30",
            "https://www.amazon.co.uk/LEGO-71709-LEGO-71709-NINJAGO-Jay-and-Lloyds-Velocity-Racers-with-Plane-and-Bike-Speeders-Prime-Empire-Racing-Vehicles/dp/B07W6Q952X/ref=sr_1_31?keywords=lego+ninjago&qid=1580830376&sr=8-31",
            "https://www.amazon.co.uk/LEGO-71711-Ninjago-Jays-Cyber-Dragon-Mech-Building-Set-with-Jay-Nya-and-Unagami-Minifigures-Prime-Empire-Action-Figures/dp/B07W6QBJ8G/ref=sr_1_42?keywords=lego+ninjago&qid=1580830376&sr=8-42",
            "https://www.amazon.co.uk/LEGO-75254-CONF_CORE9_Ep9-V29-Multicolour/dp/B07ND9SVPB/ref=sr_1_2_sspa?keywords=lego+star+wars&qid=1580913193&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySVBaRjBWWDdMSE02JmVuY3J5cHRlZElkPUEwMTY0MDA0MzZCSkk1VUdaSkgzOSZlbmNyeXB0ZWRBZElkPUExMDIyNDAwMzJGWVZLMDhTMjZJMSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
            "https://www.amazon.co.uk/LEGO-70427-LEGO-Hidden-Side-70427-Welcome-to-the-Hidden-Side-with-AR-Games-App/dp/B07WBZZLSJ/ref=sr_1_6?keywords=lego+hidden+side&qid=1580913313&sr=8-6",
            "https://www.amazon.co.uk/Ninjago-71714-LEGO-71714-NINJAGO-Kai-Avatar-Arcade-Pod-Portable-Playset-Collectible-Prime-Empire-Ninja-Toys-for-Kids/dp/B07W8XYZ2W/ref=sr_1_5?keywords=lego+ninjago+arcade%5D%23&qid=1580913458&sr=8-5",
            "https://www.amazon.co.uk/Ninjago-71716-LEGO-71716-NINJAGO-Lloyd-Avatar-Arcade-Pod-Portable-Playset-Collectible-Prime-Empire-Ninja-Toys-for-Kids/dp/B07W6Q9JYZ/ref=sr_1_6?keywords=lego+ninjago+arcade%5D%23&qid=1580913458&sr=8-6",
            "https://www.amazon.co.uk/Ninjago-71715-LEGO-71715-NINJAGO-Jay-Avatar-Arcade-Pod-Portable-Playset-Collectible-Prime-Empire-Ninja-Toys-for-Kids/dp/B07WC19M4V/ref=sr_1_4?keywords=lego+ninjago+arcade%5D%23&qid=1580913458&sr=8-4"
            ]

title_list = []

for desired in url_list:
    yes_boi = scl.get_product_details(desired)
    title = yes_boi["name"]
    print(title)
    #title_clean = [w.replace('\xa0', ' ') for w in title]
    #print(title_clean)
    title_list.append((title[5:10]))


print("Set numbers watched: ")
print(title_list)

with open('Item Numbers.txt', 'w') as file:
        file.write(str(title_list))

while True:
    price_list_print = scl.add_prices(url_list)
    #print(str(price_list_print))
    with open('Price Data.txt', 'a') as file:
        file.write(str(price_list_print)+"\n")
    print("Prices updated at "+str(datetime.datetime.now()))
    time.sleep(3600)

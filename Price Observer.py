from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def extract_lego(number):
    name_set = item_numbers.columns[number]
    price_set = [float(n.replace("[", "]").replace("]", "")) for n in list(data_raw.iloc[:, number+8])]
    print(price_set)
    return name_set, price_set

data_raw = pd.read_csv("Price Data.txt")
item_numbers = pd.read_csv("Item Numbers.txt")

dates = data_raw.iloc[:, 0:5]

years_messy = list(data_raw.iloc[:, 0])
years = [int(n[-4:-1]+n[-1]) for n in years_messy]
months = list(data_raw.iloc[:, 1])
days = list(data_raw.iloc[:, 2])
hours = list(data_raw.iloc[:, 3])
minutes = list(data_raw.iloc[:, 4])

def clean_list(list):
    new_list = []
    for n in list:
        n = "%02d" % n
        new_list.append(n)
    return new_list

days_clean = clean_list(days)
hours_clean = clean_list(hours)
months_clean = clean_list(months)
minutes_clean = clean_list(minutes)

#here we remake the datetime with fstrings
times = [f"{y},{m},{d}:{h}:{mi}" for y, m ,d ,h, mi in (zip(years, months_clean, days_clean, hours_clean, minutes_clean))]

for n in range(len(item_numbers.columns)):
    x, y = extract_lego(n-1)  
    plt.plot(times, y, label = x)
plt.xticks(rotation = 90)
plt.legend()
plt.tight_layout()
plt.show()



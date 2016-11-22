import sys
from pprint import pprint

days = []

with open('stock.txt') as f:
    lines = f.read().rstrip().split("\n")

starting_cash = float(lines.pop(0))
hours = lines.pop(0).lstrip()

for line in lines:
    this_line = line.split()
    day = {"stock": this_line.pop(0), "hours": map(float, this_line)}
    days.append(day)

def maxProfit(day, starting_cash):
    prices_at_hours = day["hours"]
    hours_to_buy = []
    hours_to_sell = []
    if all(starting_cash < stock_price for stock_price in prices_at_hours):
        return 0
    escape = 0;
    while (!everything_is_none(prices_at_hours) or escape == 1000):
        max_index = find_index_of_max(prices_at_hours)
        hours_to_sell.append(max_index)
        min_index = find_index_of_min_below_max_index(prices_at_hours, max_index)
        hours_to_buy.append(min_index)
        for i,price in enumerate(prices_at_hours):
            if i >= min_index and i <= max_index:
                prices_at_hours[i] = None
    return prices_at_hours

def find_index_of_max(prices_at_hours):
    highest_price = 0;
    index_of_highest_price = 0;
    for i,price in enumerate(prices_at_hours):
        if i == 0 or price == None or prices_at_hours[i - 1] == None:
            continue
        else:
            if price > highest_price:
                highest_price = price
                index_of_highest_price = i
    return index_of_highest_price

def find_index_of_min_below_max_index(prices_at_hours, max_index):
    min_price = None
    index_of_min_price = None;
    for i, price in enumerate(prices_at_hours[:max_index]):
        if not min_price:
            min_price = price
            index_of_min_price = i
        else:
            if price <= min_price:
                min_price = price
                index_of_min_price = i
    return index_of_min_price

def everything_is_none(some_list):
    for i in some_list:
        if i != None:
            return False
    return true









print starting_cash
print hours
pprint(days)
print maxProfit(days[0], 500)

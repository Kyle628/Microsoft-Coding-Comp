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
    hours = day["hours"]
    if all(starting_cash < stock_price for stock_price in hours):
        return 0
    lowest_price





print starting_cash
print hours
#pprint(days)
print maxProfit(days[0], 500)

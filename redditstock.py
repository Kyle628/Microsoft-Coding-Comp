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
    prices_at_hours = [999999999] + prices_at_hours
    prices_at_hours.append(-999999999)
    buy_times = []
    sell_times = []
    can_buy = True
    can_sell = False
    print prices_at_hours
    for i,price in enumerate(prices_at_hours):
        if (i == 0):
            continue
        elif (i == len(prices_at_hours) - 1):
            continue
        elif (price < prices_at_hours[i - 1] and price < prices_at_hours[i+1] and can_buy):
            buy_times.append(i);
            can_buy = False
            can_sell = True
        elif (can_sell):
            if (price >= prices_at_hours[i-1] and price > prices_at_hours[i+1]):
                sell_times.append(i)
                can_buy = True
                can_sell = False
    all_times = []
    for i,time in enumerate(buy_times):
        time -= 1
        buy_times[i] = time
    for i,time in enumerate(sell_times):
        time -= 1
        sell_times[i] = time
    for i,time in enumerate(buy_times):
        all_times.append(time)
        all_times.append(sell_times[i])
    print all_times











print starting_cash
print hours
pprint(days)
maxProfit(days[1], 500)

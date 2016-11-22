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
    og_prices_at_hours = day["hours"]
    prices_at_hours = [999999999] + prices_at_hours
    prices_at_hours.append(-999999999)
    buy_times = []
    sell_times = []
    can_buy = True
    can_sell = False
    print prices_at_hours
    print starting_cash
    for i,price in enumerate(prices_at_hours):
        if (i == 0):
            continue
        elif (i == len(prices_at_hours) - 1):
            continue
        elif (price < prices_at_hours[i - 1] and price < prices_at_hours[i+1] and can_buy and price < starting_cash):
            buy_times.append(i);
            can_buy = False
            can_sell = True
            starting_cash -= price
            print starting_cash
        elif (can_sell):
            if (price >= prices_at_hours[i-1] and price > prices_at_hours[i+1]):
                sell_times.append(i)
                can_buy = True
                can_sell = False
                starting_cash += price
    all_times = []
    end_money = starting_cash
    for i,time in enumerate(buy_times):
        time -= 1
        buy_times[i] = time
    for i,time in enumerate(sell_times):
        time -= 1
        sell_times[i] = time
    for i,time in enumerate(buy_times):
        all_times.append(time)
        all_times.append(sell_times[i])
    return {'end_money': end_money, 'buy_times': buy_times,
     'sell_times': sell_times, 'stock': day['stock']}


best_day = {'end_money': 0, 'all_times': []}
for day in days:
    day_results = maxProfit(day, starting_cash)
    if day_results['end_money'] > best_day['end_money']:
        best_day = day_results
print best_day['stock']
print best_day['end_money']
print hours
buy_times = best_day['buy_times']
sell_times = best_day['sell_times']
for i in range(0,8):
    if i in buy_times:
        if i < 2:
            sys.stdout.write("B    ")
        else:
            sys.stdout.write("B   ")
    elif i in sell_times:
        if i < 2:
            sys.stdout.write("S    ")
        else:
            sys.stdout.write("S   ")
    else:
        if i < 2:
            sys.stdout.write(".    ")
        else:
            sys.stdout.write(".   ")

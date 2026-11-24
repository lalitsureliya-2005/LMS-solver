import sys

def max_profit(values):
    if not values:
        return 0
    min_price = values[0]
    max_prof = 0
    for price in values[1:]:
        profit = price - min_price
        if profit > max_prof:
            max_prof = profit
        if price < min_price:
            min_price = price
    return max_prof

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    values = data[1:1 + n]
    print(max_profit(values))

if __name__ == "__main__":
    main()
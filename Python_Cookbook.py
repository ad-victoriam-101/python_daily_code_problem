prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
sorted_prices = sorted(zip(prices.values(),prices.keys()))
print(sorted_prices)


""" Finding Commonality between two Dictionaries """
a = {
    "a":1,
    "b":2,
    "c":3,
    "y":2,
}
b = {
    'a':10,
    'b':11,
    'x':2,
    "y":2,
}
#common keys
print(a.keys()&b.keys())
#Difference in keys
print(a.keys()-b.keys())
print(b.keys()-a.keys())

#find (key,values) pairs in dictionaries
print(a.items()&b.items())

#1.10. Removing Duplicates from a Sequence while Maintaining Order
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

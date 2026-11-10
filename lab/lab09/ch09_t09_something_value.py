prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

# 1. Create a variable called total and set it to zero
total = 0

# 2. Loop through the prices dictionary
for key in prices:
    # 3. Multiply price by stock
    item_value = prices[key] * stock[key]
    
    # 4. Print that individual item's total value
    print(item_value)
    
    # 5. Add it to the running total
    total += item_value

# 6. Finally, outside your loop, print the grand total
print(total




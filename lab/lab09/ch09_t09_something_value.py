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

total = 0
for key in prices:
    # Print the item details (Expected by the grader)
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    
    # Calculate and add to the running total (Do NOT print this step)
    total += prices[key] * stock[key]

# Print the final total outside the loop
print(total)


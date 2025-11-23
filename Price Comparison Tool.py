# Price Comparison Tool

print("=== Price Comparison Tool ===")

# Input item name
item_name = input("Enter the item name: ")

# Input number of stores
num_stores = int(input("Enter number of stores to compare: "))

stores = []
prices = []

# Collect store names and prices
for i in range(num_stores):
    store_name = input(f"Enter store #{i+1} name: ")
    store_price = float(input(f"Enter price at {store_name}: "))
    
    stores.append(store_name)
    prices.append(store_price)

# Finding the lowest price
min_price = prices[0]
best_store = stores[0]

for i in range(len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
        best_store = stores[i]

# COmparisom Result
print("\n=== Comparison Result ===")
print(f"Item: {item_name}")
print(f"Best price: ${min_price:.2f} at {best_store}")

# Full Price List
print("\nPrice List:")
for i in range(len(stores)):
    print(f"{stores[i]} - ${prices[i]:.2f}")

print("\nThank you for using the Price Comparison Tool!")
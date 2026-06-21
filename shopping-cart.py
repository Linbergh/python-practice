products = [
    ("Apple", 1.20),
    ("Bread", 2.50),
    ("Milk", 1.80),
    ("Eggs", 3.00),
    ("Butter", 4.50),
    ("Cheese", 5.20),
    ("Chicken", 8.00),
    ("Rice", 2.10),
]

cart = [products[0], products[2], products[6], products[3]]

for index, product in enumerate(products, start=1):
    print(f"{index}. {product[0]} - ${product[1]:.2f}")


print("--- Receipt ---")
total = 0

for items in cart:
    print(f"{items[0]} - {items[1]}")
    total += items[1]

print("---------------")

if total > 10:
    print(f"Total: {total}")
    print("You qualify for a 10% discount!")
    print(f"Discounted Price: {total-(total*.1)}")
else:
    print(f"Total: {total}")

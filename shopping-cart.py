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


print("Available Products:")
for index, (name, price) in enumerate(products, start=1):
    print(f"{index}. {name} - ${price:.2f}")

cart = []

while True:
    choice = int(input("Enter product number to add to cart (or 0 to checkout): "))

    if choice == 0:
        break

    if (
        not 1 <= choice <= len(products)
    ):  # If the user's choice is NOT between 1 and the number of products.
        print("Product unavailable!")
    else:
        cart.append(
            products[choice - 1]
        )  # -1 because list indexing starts at 0 (user starts at 1)
        print(f"Added {products[choice - 1][0]} to cart")


print("\n--- Receipt ---")
total = 0
for name, price in cart:
    print(f"{name} - ${price:.2f}")
    total += price
print("---------------")

print(f"Total: ${total:.2f}")

if total > 10:
    discounted = total * 0.9
    print("You qualify for a 10% discount!")
    print(f"Discounted Price: ${discounted:.2f}")

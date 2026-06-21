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


for index, product in enumerate(products, start=1):
    print(f"{index}. {product[0]} - ${product[1]:.2f}")

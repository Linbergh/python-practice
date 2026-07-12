products = [
    {"name": "Apple", "price": 1.20, "category": "Fruit", "stock": 50},
    {"name": "Bread", "price": 2.50, "category": "Bakery", "stock": 30},
    {"name": "Milk", "price": 1.80, "category": "Dairy", "stock": 20},
    {"name": "Eggs", "price": 3.00, "category": "Dairy", "stock": 15},
    {"name": "Butter", "price": 4.50, "category": "Dairy", "stock": 10},
    {"name": "Cheese", "price": 5.20, "category": "Dairy", "stock": 8},
    {"name": "Chicken", "price": 8.00, "category": "Meat", "stock": 25},
    {"name": "Rice", "price": 2.10, "category": "Grains", "stock": 40},
]


def print_product(product):
    print(
        f"{product['name']} - ${product['price']:.2f} | Category: {product['category']} | Stock: {product['stock']}"
    )


def print_all_products():
    print("----All Products----")
    for product in products:
        print_product(product)


def find_by_category(category):
    matches = [p for p in products if p["category"] == category]
    print(f"\n----{category} Products----")
    if not matches:
        print(f"No products found in category: {category}")
        return
    for product in matches:
        print_product(product)


def most_expensive():
    product = max(products, key=lambda p: p["price"])
    print(f"\nMost expensive: {product['name']} at ${product['price']:.2f}")


def out_of_stock_soon(threshold=10):
    low = [p for p in products if p["stock"] <= threshold]
    print("\n----Low Stock----")
    if not low:
        print("All products are sufficiently stocked!")
        return
    for product in low:
        print(f"Low stock warning: {product['name']} ({product['stock']} remaining)")


def summary():
    prices = [p["price"] for p in products]
    stocks = [p["stock"] for p in products]
    print("\n----Summary----")
    print(f"Total number of products: {len(products)}")
    print(f"Total combined stock: {sum(stocks)}")
    print(f"Average price: ${sum(prices) / len(prices):.2f}")


print_all_products()
find_by_category("Dairy")
most_expensive()
out_of_stock_soon()
summary()

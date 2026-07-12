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

# printing all products
for product in products:
    print(
        f"{product["name"]} - ${product["price"]:.2f} | Category: {product["category"]} | Stock: {product["stock"]}"
    )


def find_by_category(category):
    print("\n----Products by category----")
    for product in products:
        if product["category"] == category:
            print(
                f"{product["name"]} - ${product["price"]:.2f} | Category: {product["category"]} | Stock: {product["stock"]}"
            )


def most_expensive():
    prices = []

    for product in products:
        prices.append(product["price"])

    most_expensive_product = max(prices)
    product_name = products[prices.index(most_expensive_product)]["name"]

    print(f"\nMost expensive: {product_name} at ${most_expensive_product:.2f}")


def out_of_stock_soon():
    print("\n----Low Stock----")
    for product in products:
        if product["stock"] <= 10:
            print(
                f"Low stock warning: {product["name"]} ({product["stock"]} remaining)"
            )


def summary():
    prices = []
    total_stocks = 0

    for product in products:
        total_stocks += product["stock"]
        prices.append(product["price"])

    print("\n----Summary----")

    # Total number of products
    print(f"Total number of products: {len(products)}")

    # Total combined stock across all products
    print(f"Total stocks combined: {total_stocks}")

    # Average price across all products
    average_price = round(sum(prices) / len(prices), 2)
    print(f"Average price: ${average_price:.2f}")


find_by_category("Dairy")
most_expensive()
out_of_stock_soon()
summary()

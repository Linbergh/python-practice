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


def find_by_category(category):
    pass


def most_expensive(products):
    pass


def out_of_stock_soon(products):
    pass


def summary(products):
    pass

    # Total number of products

    # Total combined stock across all products

    # Average price across all products


for product in products:
    print(
        f"{product["name"]} - ${product["price"]} | Category: {product["category"]} | Stock: {product["stock"]}"
    )

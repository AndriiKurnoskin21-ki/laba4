def format_price(price):     # price: float (дробове число)
    return f"ціна: {price:.2f} грн"   # повертає str (рядок)


def check_availability(*products):   # products: tuple зі строками
    store = {
        "хліб": True,    # bool (True = є)
        "молоко": True,
        "яйця": False,   # False = немає
        "цукор": True,
        "кава": True,
        "чай": False
    }
    return {p: store.get(p, False) for p in products}   # dict (словник)


def process_order():
    prices = {          # dict: ключ — str, значення — float
        "хліб": 22.5,
        "молоко": 34,
        "яйця": 55.2,
        "цукор": 28.9,
        "кава": 99.99,
        "чай": 45.4
    }

    action = input("Дія (купити/переглянути ціну): ").lower()  # str
    products = [p.strip() for p in input("Введіть товари: ").lower().split(",")]  # list зі str

    available = check_availability(*products)  # dict

    if action == "купити":
        if all(available[p] for p in products):   # all() → bool
            total = sum(prices[p] for p in products)  # float
            print("Усі товари в наявності. " + format_price(total))
        else:
            print("Немає товарів:", [p for p in products if not available[p]])

    elif action == "переглянути ціну":
        for p in products:
            print(f"{p}: {format_price(prices.get(p, 0))}")
    else:
        print("Невідома дія!")


def main():
    process_order()


if __name__ == "__main__":
    main()

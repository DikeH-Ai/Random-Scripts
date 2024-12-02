def main():
    order()

def order():
    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    y = 0
    while True:
        try:
            item = input("Item: ").strip().title()
            x = items[item]
            y += x
        except(EOFError):
            return print()
        except(KeyError):
            pass
        else:
            print(f"Total: ${y:.2f}")
main()
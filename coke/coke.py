def main():
    coke_machine()

def coke_machine():
    coke_price = 50
    while coke_price > 0:
        print(f"Amount Due: {coke_price}")
        user_input = int(input("Insert coin: "))
        if user_input in [25,5,10]:
            coke_price = coke_price - user_input
        else:
            continue
    print(f"Change Due: {abs(coke_price)}")


main()
def main():
    greeting = input("Greetings: ").lower().strip()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h", 0,2):
        print("$20")
    else:
        print("$100")

main()
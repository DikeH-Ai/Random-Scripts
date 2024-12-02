# main function
def main():
    camel_case =  input("camelCase: ").strip()
    print("snake_case: ", end="")
    converter(camel_case)


def converter(camel_case):
    for i in camel_case:
        if i.isupper():
            print("_", end="")
        print(i.lower(), end="")
    print()

main()
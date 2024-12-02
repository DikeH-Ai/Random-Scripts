def main():
    x = guage()
    if x < 2:
        print("E")
    elif x > 98:
        print("F")
    else:
        print(f"{x}%")

def guage():
    while True:
        fractions = input("Fractions: ").split("/")
        try:
            x,y = int(fractions[0]),int(fractions[1])
        except(ValueError, ZeroDivisionError, IndexError):
            pass
        else:
            if x <= y:
                return round((x / y) * 100)
            else:
                pass

main()
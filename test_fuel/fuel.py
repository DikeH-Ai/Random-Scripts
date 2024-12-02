def main():
    x = gauge()
    if x < 2:
        print("E")
    elif x > 98:
        print("F")
    else:
        print(f"{x}%")



def convert(fraction):
    while True:
        try:
            fraction.split("/")
            x,y = int(fraction[0]),int(fraction[1])
        except(ValueError, ZeroDivisionError, IndexError):
            pass
        else:
            if x <= y:
                return round((x / y) * 100)
            else:
                pass


def gauge(percentage):
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
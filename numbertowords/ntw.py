# 1-100000 in words
def main():
    number = input("Number: ")
    ntw(number)


def ntw(number: str):
    num_len = len(number)
    if num_len == 1:
        print(unit(number))
    elif num_len == 2:
        print(tens(number))
    elif num_len == 3:
        print(hundred(number))
        print(tens(number))
    elif num_len == 4:
        print(thousand(number))
    elif num_len == 5:
        print(tens_of_thousand(number))
    else:
        print("Beyond maximum digit")


def unit(number: str):
    if len(number) != 1:
        return
    unit_dict = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    return (unit_dict[number])


def tens(number):
    if len(number) != 2:
        return
    tens_dict = {
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen",
        "20": "Twenty",
        "30": "Thirty",
        "40": "Fourty",
        "50": "Fifty",
        "60": "Sixty",
        "70": "Seventy",
        "80": "Eighty",
        "90": "Ninety",
    }
    if number in tens_dict:
        return (tens_dict[number])
    else:
        return tens_dict[number[0]+"0"] + " " + unit(number[1])


def hundred(number):
    if len(number) != 3:
        return
    hundred_dict = {
        "100": "One Hundred",
        "200": "Two Hundred",
        "300": "Three Hundred",
        "400": "Four Hundred",
        "500": "Five Hundred",
        "600": "Six Hundred",
        "700": "Seven Hundred",
        "800": "Eight Hundred",
        "900": "Nine Hundred",
    }
    if number in hundred_dict:
        return (hundred_dict[number])
    else:
        return hundred_dict[number[0]+"00"] + " and " + tens(number[1:])


def thousand(number):
    if len(number) != 4:
        return
    thou = unit(number[0]) + " thousand"
    if int(number[1:]) < 1:
        return thou
    if int(number[1]) > 0:
        hun = hundred(number[1:])
        return thou + " " + hun
    else:
        hun = "and"
    if int(number[2]) > 0:
        ten = tens(number[2:])
        return thou+" " + hun + " " + ten
    if int(number[3]) > 0:
        uni = unit(number[3])
        return thou+" " + hun + " " + uni


def hundreds_of_thousand(number: str):
    pass


def tens_of_thousand(number):
    ten = tens(number[:2]) + " " + "thousand"
    if int(number[2]) > 0:
        hun = hundred(number[2:])
        return ten + ' ' + hun
    if int(number[3]) > 0:
        ten1 = tens(number[3:])
        return ten + ' ' + ten1
    if int(number[4]) > 0:
        ten1 = tens(number[3:])
        return ten + ' ' + ten1


if __name__ == "__main__":
    main()

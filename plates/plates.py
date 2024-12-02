def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate[0:2].isnumeric():
        return False
    if len(plate) < 2 or len(plate) > 6:
        return False
    for i in plate:
        if i.isnumeric():
            if i == "0":
                return False
            break
    case = '''\,<>./?@#$!()-[]{};:'"%^&*_~'''
    for i in plate:
        if i in case:
            return False
    if " " in plate:
        return False
    mid = round((len(plate) / 2) - 1)
    if plate[mid].isnumeric():
        if plate[mid:].isalnum():
            return False
    return True

main()
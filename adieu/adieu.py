# create a function
# prompt for name in a forever loop
# check for Eoferror and return print
# append names to list '
import inflect
p = inflect.engine()

names = []

def adieu():
    while True:
        try:
            x = input("Name: ").strip()
            names.append(x)
        except(EOFError):
            if len(names) > 1:
                mylist = p.join(names)
                return print(f"Adieu, adieu, to {mylist}")
            elif len(names) == 1:
                return print(f"Adieu, adieu, to {names[0]}")
            else:
                return print()

adieu()

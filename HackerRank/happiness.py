def happiness_guage(seta: set, setb: set, array: list) -> int:
    happiness = 0
    for i in array:
        if i in seta:
            happiness += 1
        elif i in setb:
            happiness -= 1
    return happiness


if __name__ == "__main__":
    n, m = input().split(" ")
    array = input().split(" ")
    seta = input().split(" ")
    setb = input().split(" ")
    seta = set(seta)
    setb = set(setb)
    happi = happiness_guage(seta=seta, setb=setb, array=array)
    print(n, m, seta, setb, array, happi)

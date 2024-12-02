def main():
    grocery()

def grocery():
    dic = {}
    while True:
        try:
            x = input().strip().upper()
        except(EOFError):
            print()
            break
        else:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1
    # looping through keys and values ref: https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp
    for i,j in sorted(dic.items()):
        print(j,i)


main()
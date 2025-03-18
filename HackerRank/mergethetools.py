def main():
    v = "AABCAAADA"
    k = 3

    for i in range((len(v)//k)):
        substring = v[i*k: k*(i+1)]
        # remove duplicate
        for x, j in enumerate(substring):
            if j not in substring[:x]:
                print(j, end="")
        print()


if __name__ == "__main__":
    main()

def main():
    list1, list2 = get_data("data.txt")
    similarity_list(list1, list2)
    print(praser(list1, list2))

# get user data return 2 list


def get_data(filename: str):
    list1 = []
    list2 = []
   # read data from file
    with open(filename, "r") as f:
        file = f.readlines()
        for i in file:
            a, b = i.strip("\n").split("  ")
            list1.append(int(a))
            list2.append(int(b))

    return list1, list2

# prase data


def praser(data: list, data1: list):
    # find the difference between list
    data.sort()
    data1.sort()
    result = [abs(a - b) for a, b in zip(data, data1)]
    return sum(result)


def similarity_list(list1: list, list2: list) -> int:
    # find the similarity between list
    list1.sort()
    list2.sort()
    result = []
    for i in list1:
        counter = 0
        for j in list2:
            if i < j:
                break
            if i == j:
                counter += 1
        result.append(counter * i)
    print(sum(result))


if __name__ == "__main__":
    main()

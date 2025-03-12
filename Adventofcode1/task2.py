def main():
    data_list = read_data("data2")
    number = filtered_list(data_list)
    print(number)


def read_data(filename: str) -> list:
    file_data = []
    with open(filename, "r") as fd:
        file_data = fd.readlines()
        # parse data/ remove /n character/ split items
        file_data = list(map(lambda x: x.strip("\n").split(" "), file_data))
        # convert to int
        file_data = list(
            map(lambda sublist: [int(x) for x in sublist], file_data))
        # file_data = [i.strip("\n") for i in file_data]
    return file_data


def filtered_list(data: list) -> list:
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    new_list = []
    for sublist in data:
        if all(abs(x - sublist[idx + 1]) in range(0, 4) for idx, x in enumerate(sublist[:-1])):
            count = 0
            if sublist[0] > sublist[1]:
                # decreasing order
                for idx, x in enumerate(sublist[1:]):
                    if sublist[idx - 1] < x:
                        count += 1
                if count > 1:
                    continue
                # if tmplist != sorted(sublist, reverse=True):
                #     continue
            else:
                # ascending order
                for idx, x in enumerate(sublist[1:]):
                    if sublist[idx - 1] > x:
                        count += 1
                if count > 1:
                    continue
                # if tmplist != sorted(sublist):
                #     continue
            new_list.append(sublist)
    return len(new_list)


if __name__ == "__main__":
    # filtered_list([[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [
    #               1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]])
    main()

def main():
    outdated()


def outdated():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        month_day_year = input("Date: ").strip()

        if "/" in month_day_year:
            try:
                month_day_year = month_day_year.split('/')
                month = int(month_day_year[0])
                day = int(month_day_year[1])
                year = int(month_day_year[2])
            except(ValueError,IndexError):
                continue

            else:
                if month < 13 and day < 32:

                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:

                    continue

        else:
            try:
                month_day_year = month_day_year.split(',')
                year = int(month_day_year[1])
                month_day = month_day_year[0].split()
                month = month_day[0]
                day = int(month_day[1])
            except(ValueError,IndexError):
                continue

            else:
                if month in months and day < 32:
                    month = (months.index(month) + 1)

                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue

main()
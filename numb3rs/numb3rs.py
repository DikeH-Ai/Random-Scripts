import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    result = re.search(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",ip)
    if result:
        if int(result.group(1)) > 255 or int(result.group(2)) > 255 or int(result.group(3)) > 255 or int(result.group(4)) > 255:
            return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
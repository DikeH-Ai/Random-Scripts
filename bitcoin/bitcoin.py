import sys
import requests

def main():
    bitcoin_price()

def bitcoin_price():
    # Expects the user to specify as a command-line argument the number of Bitcoins, , that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
    try:
        sys.argv[1] = float(sys.argv[1])
    except(ValueError, IndexError):
        sys.exit("Parameter Error")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()
    except(requests.RequestException):
        sys.exit("Request Error")
    else:
        amount = response["bpi"]["USD"]["rate_float"]
        amount =  amount * sys.argv[1]
        return print(f"${amount:,.4f}")

main()
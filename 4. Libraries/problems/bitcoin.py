import sys
from requests import get, RequestException


def main():
    amount_of_bitcoin = check_arguments()
    bitcoin_value = get_bitcoin_value()
    result = (bitcoin_value * amount_of_bitcoin)
    print(f"${result:,}")


def check_arguments():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        number_of_bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    return number_of_bitcoin


def get_bitcoin_value():
    try:
        response = get("https://api.coindesk.com/v1/bpi/currentprice.json")

    except RequestException:
        sys.exit("Unexpected exception occured with the API response")

    json_response = response.json()

    bitcoin_value = float(json_response["bpi"]["USD"]["rate"].replace(",", ""))

    return bitcoin_value


if __name__ == "__main__":
    main()

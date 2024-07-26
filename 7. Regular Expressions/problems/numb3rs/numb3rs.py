import re


def main():
    ip_address = input("IPv4 Address: ").strip()
    print(validate(ip_address))


def validate(ip_address):
    if not is_valid_format(ip_address):
        return False

    octets = map(int, ip_address.split("."))
    return all(0 <= octet <= 255 for octet in octets)


def is_valid_format(ip_address):
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    return re.match(pattern, ip_address) is not None


if __name__ == "__main__":
    main()

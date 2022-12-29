import hashlib


def main():
    secret_key = 'bgvyzdsv'
    number = 0
    santa_hash = ""
    byte_string = (secret_key + str(number)).encode()
    santa_hash = hashlib.md5(byte_string)
    while santa_hash.hexdigest()[:6] != "000000":
        number += 1
        byte_string = (secret_key + str(number)).encode()
        santa_hash = hashlib.md5(byte_string)
    print(number, santa_hash.hexdigest())


if __name__ == "__main__":
    main()

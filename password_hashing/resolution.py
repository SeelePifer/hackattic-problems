import hashlib
import hmac
import binascii
import base64
from hashlib import pbkdf2_hmac

import requests
from Crypto.Protocol.KDF import scrypt


def main():
    get_url = "https://hackattic.com//challenges/password_hashing/problem?access_token=a40a9cc04aa86fdf"

    response = requests.get(get_url)

    if response.status_code == 200:
        data = response.json()

        password = data['password'].encode()
        salt = base64.b64decode(data['salt'])

        sha256 = hashlib.sha256(password).hexdigest()

        hmac_sha256 = hmac.new(salt, password, hashlib.sha256).hexdigest()

        pbkdf2_sha256 = pbkdf2_hmac('sha256', password, salt, data['pbkdf2']['rounds'])
        pbkdf2_sha256_hex = binascii.hexlify(pbkdf2_sha256).decode()

        scrypt_hash = scrypt(password, salt, key_len=data['scrypt']['buflen'], N=data['scrypt']['N'],
                             r=data['scrypt']['r'], p=data['scrypt']['p'])
        scrypt_hash_hex = binascii.hexlify(scrypt_hash).decode()

        post_url = "https://hackattic.com/challenges/password_hashing/solve?access_token=a40a9cc04aa86fdf"

        solution = {
            "sha256": sha256,
            "hmac": hmac_sha256,
            "pbkdf2": pbkdf2_sha256_hex,
            "scrypt": scrypt_hash_hex
        }
        response = requests.post(post_url, json=solution)
        if response.status_code == 200:
            print(response.json())
        else:
            print(response.text)
    else:
        print(response.text)


if __name__ == "__main__":
    main()

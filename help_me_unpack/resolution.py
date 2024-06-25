import json

import requests
import struct
import base64


def main():
    base_path = "https://hackattic.com"
    problem_url = f"{base_path}/challenges/help_me_unpack/problem?access_token=a40a9cc04aa86fdf"
    solution_url = f"{base_path}/challenges/help_me_unpack/solve?access_token=a40a9cc04aa86fdf"

    response = requests.get(problem_url)
    data = response.json()

    bytes_data = base64.b64decode(data["bytes"])
    print(len(bytes_data))
    myint = struct.unpack('<i', bytes_data[:4])[0]
    uint = struct.unpack("<I", bytes_data[4:8])[0]
    short = struct.unpack("<h", bytes_data[8:10])[0]
    myfloat = struct.unpack("<f", bytes_data[12:16])[0]
    double = struct.unpack("<d", bytes_data[16:24])[0]
    bige_double = struct.unpack(">d", bytes_data[24:32])[0]

    data = json.dumps({'int': myint,
                  'uint': uint,
                  'short': short,
                  'float': myfloat,
                  'double': double,
                  'big_endian_double': bige_double
                  })
    response = requests.post(solution_url, data=data)
    print(response.json())


if __name__ == "__main__":
    main()

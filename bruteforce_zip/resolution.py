import requests
import shutil
import subprocess
from subprocess import call

def main():
    response = requests.get("https://hackattic.com/challenges/brute_force_zip/problem?access_token=a40a9cc04aa86fdf")
    json_response = response.json()

    zip_url = json_response["zip_url"]
    response = requests.get(zip_url, stream=True)
    with open('package.zip', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    proc = subprocess.Popen(['fcrackzip', 'package.zip', '-c', 'a1', '-l', '4-6', '-v', '-u'],stdout=subprocess.PIPE)
    while True:
      line = proc.stdout.readline()
      if not line:
        break
      ans = line

    ans = ans.replace(b'PASSWORD FOUND!!!!: pw == ', b'')
    ans = ans.replace(b'\n', b'')
    print(ans.decode())

    proc = call(['unzip', '-P', ans, 'package.zip'])

    with open('secret.txt', 'r') as f:
        lines = f.readlines()

    print(len(lines))
    print(lines[0].rstrip())
    response = requests.post("https://hackattic.com/challenges/brute_force_zip/solve?access_token=a40a9cc04aa86fdf", json={'secret': lines[0].rstrip()})
    print(response.content)
if __name__ == "__main__":
    main()
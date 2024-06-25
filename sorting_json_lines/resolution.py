import json
import sys

def main():
    accounts = {}

    for line in sys.stdin:
        line = line.strip()
        data = json.loads(line)
        for name, info in data.items():
            if name == 'extra':
                continue
            if 'extra' in data:
                balance = data['extra']['balance']
            else:
                balance = info['balance']
            accounts[name] = balance

    sorted_accounts = sorted(accounts.items(), key=lambda x: x[1])

    for name, balance in sorted_accounts:
        print(f"{name}: {balance:,}")

if __name__ == "__main__":
    main()
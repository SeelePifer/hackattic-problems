import sys
def main():
    for line in sys.stdin:
        line = line.strip()
        binary_str = line.replace('#','1').replace('.','0')
        number = int(binary_str, 2)
        print(number)
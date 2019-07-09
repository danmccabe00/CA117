import sys

b = ["e", "v", "i", "l"]
def main():
    for lines in sys.stdin:
        a = []
        for l in lines.strip().lower():
            if l == "e" or l == "v" or l == "i" or l == "l":
               a.append(l)
        if a == b:
            print(lines.strip())

if __name__ == '__main__':
    main()

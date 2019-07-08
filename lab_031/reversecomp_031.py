import sys

def revcmp(words):
   valid = {word.lower(): True for word in words if len(word) >= 5}
   words = [word for word in words if word.lower()[::-1] in valid]
   print(words)
   return words

def main():
   words = [word.strip() for word in sys.stdin]
   revcmp(words)

if __name__ == "__main__":
    main()

import sys

def main():
   try:
      with open(sys.argv[1]) as f:
         bestmark = - 1
         for line in f:
            mark, name = line.strip().split(" ", 1)
            if bestmark < int(mark):
               bestmark, beststudent = int(mark), name
            elif int(mark) == bestmark:
               beststudent + ", " + name
      print("Best student:", beststudent)
      print("Best mark:", bestmark)

   except FileNotFoundError:
      print("The file", sys.argv[1], "could not be opened.")

   except ValueError:
      print("Invalid mark", mark, "encountered. Exiting.")

if __name__ == '__main__':
   main()

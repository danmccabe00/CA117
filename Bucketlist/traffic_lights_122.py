import sys

def wait(eliza, red, green):
   time = 0
   i = 0
   while time <= eliza:
      if i == 0:
         time = time + int(red)
         i = i + 1
      elif i == 1:
         time = time + int(green)
         i = i - 1
   if i == 1:
      wait = time - eliza
   elif i == 0:
      wait = 0
   return(wait)

def main():
   lights = sys.stdin.readlines()
   road = lights[0]
   eliza = 0
   i = 1
   old_dist = "0"
   while i < len(lights):
      dist, red, green = lights[i].strip().split()
      eliza = eliza + (int(dist) - int(old_dist))
      eliza = eliza + wait(eliza, red, green)
      i = i + 1
      old_dist = dist
   eliza = eliza + (int(road) - int(old_dist))
   print(eliza)

if __name__ == '__main__':
   main()

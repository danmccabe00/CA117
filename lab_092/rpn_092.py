from stack_092 import Stack

def cal(sym, p1, p2):
   if sym == "+":
      return p1 + p2
   elif sym == "-":
      return p2 - p1
   elif sym == "*":
      return p1 * p2
   elif sym == "/":
      return p2 / p1

def cal2(sym, p):
   if sym == "n":
      return -p
   elif sym == "r":
      return p ** (1 / 2)

def calculator(line):
   s = Stack()
   d = ["+", "-", "*", "/"]
   d2 = ["r", "n"]
   l = line.split()
   for chars in l:
      if chars not in d and chars not in d2:
         s.push(chars)
      elif chars in d:
         p1 = float(s.pop())
         p2 = float(s.pop())
         s.push(cal(chars, p1, p2))
      elif chars in d2:
         p = float(s.pop())
         s.push(cal2(chars, p))

   return float(s.top())

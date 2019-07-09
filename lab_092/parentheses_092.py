from stack_092 import Stack
def matcher(line):
   s = Stack()
   for char in line:
      if char == "(" or char == "{" or char == "[":
         s.push(char)
      elif char == ")" or char == "}" or char == "]":
         try:
            if not s.is_empty:
               return False
            elif char == ")" and s.top() == "(":
               s.pop()
            elif char == "}" and s.top() == "{":
               s.pop()
            elif char == "]" and s.top() == "[":
               s.pop()
            else:
               return False
         except:
            return False
   return s.is_empty()

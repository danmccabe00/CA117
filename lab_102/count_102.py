def count_letters(s):
   if len(s) == 0:
      return 0

   else:
      return len(s) + count_letters(s[len(s):])

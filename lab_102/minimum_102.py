def minimum(l):
   if len(l) == 1:
      return l[0]

   minnum = minimum(l[:-1])
   if l[-1] < minnum:
      return l[-1]
   else:
      return minnum

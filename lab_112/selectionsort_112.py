def selectionsort(t):
   i = 0
   while i < len(t):
      p = i
      j = i + 1
      while j < len(t):
         if int(t[j]) < int(t[p]):
            p = j
         j = j + 1
      tmp = t[p]
      t[p] = t[i]
      t[i] = tmp
      i = i + 1

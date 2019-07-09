import sys

def main():
   lines = []
   d = {}

   for line in sys.stdin:
      lines.append(line.strip())
   letters, words = lines[0].split()
   letters = int(letters)
   letterslist = lines[1:letters + 1]

   for l in letterslist:
      if l[0] not in d:
         d[l[0]] = set(l[2])
      else:
         d[l[0]].add(l[2])

   i = 0
   while i < len(letterslist):
      for t in letterslist:
         if t[2] in d:
            d[t[0]] = d[t[0]] | d[t[2]]
      i = i + 1

   wordslist = lines[letters + 1:]
   for chars in wordslist:
      word1, word2 = chars.split()
      if len(word1) == len(word2):
         i = 0
         tot = 0
         while i < len(word1):
            if word1[i] != word2[i]:
               try:
                  if word2[i] in d[word1[i]]:
                     pass
                     #print("yes")
                  else:
                     #print("no")
                     tot = tot + 1
               except:
                  #print("no")
                  tot = tot + 1
            i = i + 1
         if 0 < tot:
            print("no")
         else:
            print("yes")

      else:
         print("no")
if __name__ == '__main__':
   main()

from operator import itemgetter
word2count = {}
words = []
f = "Articles are words that define a noun as specific or unspecific. Consider the following examples: After the long day, the cup of tea tasted particularly good. By using the article the, we've shown that it was one specific day that was long and one specific cup of tea that tasted good."
data = f.split()
for i in data:
    words.append(i)

print("------Mapper Output--------")

for word in words:
    
 print ('%s %s' % (word, 1))
    

print("------Reducer Output-------")

for word in words:    
    
 word,count = word,1
    
 try:
        
    count = int(count)
        
    word2count[word] = word2count.get(word, 0) + count
    
 except ValueError:
  
      pass

sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

for word,count in sorted_word2count:
    
 print ('%s %s'% (word, count))
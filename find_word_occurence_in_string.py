s = str(s)
wordCount = 0
i=0
for i in range(len(s)-2):
    word = str(s[i]+s[i+1]+s[i+2])
    if word == 'bob':
        wordCount = wordCount + 1
print("Number of words: " + str(wordCount))

s = str(s)
numVowels = 0
for vowels in s:
    if vowels == 'a' or vowels == 'e' or vowels == 'i' or vowels == 'o' or vowels == 'u':
        numVowels = numVowels + 1
print("Number of Vowels: " + str(numVowels))

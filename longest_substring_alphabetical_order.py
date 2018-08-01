s = str(s)
previous = ""
current = ""
longest = ""
for char in s:
    if previous <= char:
        current = current + char
        if len(current) > len(longest):
            longest = current
    else:
        current = char
    previous = char
print(longest)
 

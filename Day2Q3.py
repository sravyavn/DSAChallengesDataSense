#Day2Q3: length of last word
s="Learn python, coding is fun  "
s=s.strip()
count=0
lastword=""
i=len(s)-1
while s[i]!=" ":
    count+=1
    i-=1
print(count)
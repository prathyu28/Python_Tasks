s=input()
s=s.lower()
lst=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            temp=s[i:j+1]
            rev=temp[::-1]
            if(temp==rev):
                lst.append(temp)
print(lst)
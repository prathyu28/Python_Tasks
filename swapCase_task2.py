s=input()
val=[]
for i in s:
    val.append(ord(i))
for i in range(len(val)):
    if val[i]>=97 and val[i]<=122:
        val[i]-=32
    elif val[i]>=65 and val[i]<=90:
        val[i]+=32
new_str=''
for i in val:
    new_str+=chr(i)
print(new_str)
import sys
def binary(n):
    print(n)
    s=''
    while n>0:
        s+=str(int(n%2))
        n=n//2
    return s[::-1]
if(sys.argv[1].isdigit()):
    print(binary(int(sys.argv[1])))
else:
    print(binary(ord(sys.argv[1])))

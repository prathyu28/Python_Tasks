val=input("Enter input")
if(val.isdigit()):
    n=bin(int(val))
    print("Binary number:",n[2:])
else:
    n=bin(ord(val))
    print("Binary number:",n[2:])
    

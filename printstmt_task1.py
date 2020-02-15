for number in range(1,101):
    if(number%3==0 and number%5==0):
        print("Placements",end=' ')
    elif(number%3==0):
        print("Prathyusha",end=' ')
    elif(number%5==0):
        print("Pavan",end=' ')
    else:
        print(number,end=' ')
        
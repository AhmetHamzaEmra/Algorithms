def findFactors(number):
    f=[]
    i=2
    while(i<number):
        while(number%i==0):
            f.append(i)
            number=number//i
        i+=1
    if number>1:
        f.append(number)
    return f

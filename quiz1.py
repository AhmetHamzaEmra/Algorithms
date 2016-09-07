def findFactors(n):
    factors=[]
    i=2
    while(i<n):
        while (n%i==0):
            factors.append(i)
            n=n/i
        i+=1
    if (n>1):
        factors.append(int(n))
    return factors
print (findFactors(30))

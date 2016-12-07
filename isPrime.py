def IsPrime(n):
    if n==2:
        return True
    if n<=1 or n%2==0:
        return False
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return False
                break
            i+=2
    return True
    

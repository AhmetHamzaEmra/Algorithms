def RaiseToPower():
    a = eval(input("Number  you want to take power"))
    p = eval(input("Power:"))
    i = 1
    result = 1
    while (p >= 1):
        if (p % 2) == 1:
            result  = result * a

        p = p/2
        a = a * a

    return result
print (RaiseToPower())

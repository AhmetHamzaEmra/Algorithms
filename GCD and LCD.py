#Integer: GCD(Integer: A, Integer: B)
#While (B != 0)
#Integer: remainder = A Mod B
#// GCD(A, B) = GCD(B, remainder)
#A = B
#B = remainder
#End While
#Return A
#End GCD


def GCD(a, b):
    while(b!=0):
        remainder=a%b
        a=b
        b=remainder
    return a
def LCD(a,b):
    return a*b/GCD(a,b)

x= LCD(32, 20)
print (x)

from __future__ import print_function


A=[9,8,7,6,5,4,3,2,1]
B=[]
C=[]

def towerOfHanoi(from_peg, to_peg, other_peg, n):
    if n>0:
        towerOfHanoi(from_peg,other_peg,to_peg,n-1)
        to_peg.append(from_peg.pop())
        print(A, B, C, '------------', sep='\n')
        towerOfHanoi(other_peg, to_peg, from_peg, n - 1)


towerOfHanoi(A,C,B,9)

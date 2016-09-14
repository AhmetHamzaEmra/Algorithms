import random
def randomizeArray(arr):
    max=len(arr)-1
    for i in range(max-1):
        j=random.randint(i,max)
        a=arr[i]
        arr[i]=arr[j]
        arr[j]=a
a=["Talgat", "Hamza", "Behic", "adsasd", "masa", "ps"]
randomizeArray(a)
print (a)

def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        value=arr[i]
        pos=i
        while pos>0 and value <arr[pos-1]:
            arr[pos]=arr[pos-1]
            pos-=1
        arr[pos]=value
    return (arr)

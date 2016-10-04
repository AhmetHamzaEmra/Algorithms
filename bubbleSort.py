def bubbleSort(ar):
    not_sorted=True
    while(not_sorted):
        not_sorted=False
        for i in range(1,len(ar)):
            if (ar[i]<ar[i-1]):
                temp=ar[i]
                ar[i]=ar[i-1]
                ar[i-1]=temp
                not_sorted=True
    return ar

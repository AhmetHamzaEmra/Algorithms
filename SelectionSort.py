def SelectionsSort(ar):
    for i in range(len(ar)-1):
        smallest=i
        for j in range(i+1,len(ar)):
            if ar[j]<ar[smallest]:
                smallest=j
        if ar[i]>ar[smallest]:
            a=ar[i]
            ar[i]=ar[smallest]
            ar[smallest]=a
    return ar

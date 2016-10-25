def swap(arr,x,y):
    mem = arr[x]
    arr[x] = arr[y]
    arr[y] = mem
    return arr

def qsort(ar,start,end):
    # base case
    if end-start <= 0:
        return ar
    # pivot
    pivot = ar[end]
    # init index for pivot
    ind = start
    # loop less final value (pivot)
    for i in range(start,end):
        if ar[i] <= pivot:
            ar = swap(ar,i,ind)
            ind += 1
        else:
            pass
    swap(ar,ind,end)
    # left side
    ar = qsort(ar,start,ind-1)
    # right side
    ar = qsort(ar,ind+1,end)
    return ar

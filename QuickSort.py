def QuickSort(ar):
    less=[]
    more=[]
    pivotlist=[]
    if len(ar)<=1:
        return ar
    else:
        pivot=ar[0]
        for i in ar:
            if i<pivot:
                less.append(i)
            elif i>pivot:
                more.append(i)
            else:
                pivotlist.append(i)
        less=QuickSort(less)
        more=QuickSort(more)
        return less+pivotlist+more


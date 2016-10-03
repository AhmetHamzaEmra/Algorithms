def CountingSort(ar, max_value):
    counts=[]
    for i in range(max_value+1):
        counts.append(0)
    
    for i in range(len(ar)):
        counts[ar[i]]=counts[ar[i]]+1
        
    sortedList = []
    for i in range(max_value+1):
        if counts[i] > 0:
            for j in range(counts[i]):
                sortedList.append(i)
    return sortedList

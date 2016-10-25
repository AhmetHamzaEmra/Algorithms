def quicksort(values,start,end):
    if start>=end:
        return 
    divider=values[start]
    lo=start
    hi=end
    while True:
        while(values[hi]>=divider):
            hi-=1
            if hi<=lo:
                break
        if hi<=lo:
            values[lo]=divider
            break
        values[lo]=values[hi]
        
        lo+=1
        while (values[lo]< divider):
            lo+=1
            if lo>=hi:
                break
        if lo>=hi:
            lo=hi
            values[hi]=divider
            
        values[hi]=values[lo]
    quicksort(values, start, lo-1)
    quicksort(values, lo+1, end)
    return values

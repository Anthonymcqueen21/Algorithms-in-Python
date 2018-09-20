def partition(arr,low,high):
    i = (low-1)  #index of smaller element
    
    pivot = arr[high]
        for j in range(low,high): # If the current element is smaller

# Insertion sort is about rearranging elements

# Implementation

def insertion_sort(arr):
  for k in range(1, len(arr)):
     key = arr[k]
     j = k
     while j > 0 and arr[j-1]
  > arr[j]:
       arr[j], arr[j-1] = arr[j-1], arr[j]
          j = j - 1

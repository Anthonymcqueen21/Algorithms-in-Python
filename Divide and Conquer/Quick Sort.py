# Again another algorithm that breaks down problems into smaller problems in terms command and conquer.

# Implementation
from random import randint
def quicksort(lst, start, end):
   if start < end:
      pivot = randint(start, end)
      
      # swap with the last element
lst[end],lst[pivot] = lst[pivot],lst[end]
     # partition the list
     split = partition(lst, start, end)
     # sort both halves
     quicksort(lst, start, split-1)
     quicksort(lst, split+1, end)
      

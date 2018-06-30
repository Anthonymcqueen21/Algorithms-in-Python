# This particular algorithm is used to break down problems into smaller chunks.

# Implementation

def merge_sort(list):
   if len(list) < 2:
      return list
      
   mid = len(list)//2
   left = merge_sort(list[:mid])
   right = merge_sort(list[mid:])
   
return merge(left, right)
   
   

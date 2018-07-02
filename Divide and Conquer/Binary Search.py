# One of the fastest search algorithms for sorting list

#Implementation

def binary_search(my_list, l, r, x):
   if r >= 1:
     mid = l + (r - l)//2
     if my_list(mid) == x:
       return mid
     elif my_list[mid] > x:
       return binary_search(my_list, l, mid-1, x)
     else:
       return binary_search(my_list, mid+1, r, x)
     else:
       return -1

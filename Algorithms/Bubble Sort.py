# Bubble sorting is an algorithm which is used to sort a list of elements in arrays.

# Implementation
# Python Script
def bubble_sort(nlist):
   for passnum in
for i in range(len(nlist)-1,0,-1):
   for j in range(passnum):
      if nlist[j]>nlist[j+1]:
   nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
   
return bubble_sort

   
# Defining num_swaps and count_swaps in a problem statement

def countSwaps(lst):
    num_swaps = 0
    if len(lst) < 2:
        return num_swaps
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1],lst[j]
                num_swaps += 1
return num_swaps

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
      
swaps = countSwaps(a)
      
print('Array is sorted in {0} swaps.'.format(swaps))
print('First Element: {0}'.format(a[0]))
print('Last Element: {0}'.format(a[-1]))

# Linear search is a algorithm that searches for a missing element

#Implementation 
def search(x, my_list):
   for k in range(len(my_list)):
     if my_list[k] == x:
       return k
     return - 1

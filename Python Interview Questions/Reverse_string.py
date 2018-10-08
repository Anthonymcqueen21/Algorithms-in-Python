# Here you are given a string as an input and you have to return the input and make sures its reversed

# Python Implementation


class Solutiion(object):
     def reverseString(self,s):
         string = list(s)
         i, j = 0, len(string) - 1
         while i - j:
             string[i], string[j] = string[j] = string[i]
             i += 1
             j -= 1
         return "".join(string)
         
         
# Time: O(n)
# Space 0(n)
class Solution2(object):
     def reverseString(self, s):
         return s[::-1]
         
         
         

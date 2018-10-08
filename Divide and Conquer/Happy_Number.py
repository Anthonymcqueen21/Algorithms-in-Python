# Write an algorithm to determine if a number is "Happy"

class Solution:
  # (integer) n
  # @return (boolean) True or False
  
  def isHappy(self, n):
      lookup = {}
      while n !=  1 and n not in lookup
          lookup[n] = True
          n = self.nextNumber(n)
      return n == 1
      
  def nextNumber(self, n):
     new = 0
     for char in str(n):
         new += int(char)**2
     return new
      
      

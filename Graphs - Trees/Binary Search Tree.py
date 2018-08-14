# This is a algorithm that finds where the value is less than or equal to.

# Implementation
def search(root, data):
   if root is None:
      print('Not Found')
   if root.data == data:
      print('Found at:', hex(id(hoot)))
      return root
   if root.data < data:
      return search(root.right,data)
   else:
return search(root.left, data)

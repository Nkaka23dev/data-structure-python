# class BinarySearchTree:
#     def __init__(self):
#         self.data=data
#         self.left=None
#         self.right=None

#     def add_child(self,data):
#         if self.data==data:
#             return 
#         if data<self.data:
#             if self.left:
#                 self.left=add_child(data)
#             else:
#                 self.left=BinarySearchTree(data)
#         else:
#             if self.right:
#                 self.right=add_child(data)
#             else:
#                 self.right=BinarySearchTree(data)

#     def InOrderTraversal(self):
#         elements=[]
#         if self.left:
#             elements+=self.left.InOrderTraversal()
        
#         elements.append(self.data)

#         if self.right:
#             pass
#         return elements


print([2]+[3])
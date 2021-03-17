# class Node:
#     def __init__(self,data=None,nex=None,prev=None):
#         self.data=data
#         self.next=nex
#         self.prev=prev
    
# nodeA=Node(10)
# nodeB=Node(3)
# nodeC=Node(6)

# nodeA.next=nodeB
# nodeB.next=nodeC
# nodeB.prev=nodeA

# def nodeCount(head):
#     count=0
#     current_node=head
#     while current_node!=None:
#         current_node=current_node.next
#         count+=1
#     return count

# print(nodeCount(nodeA))
# print(nodeB.prev.data)
# print(nodeA.next.next.data)
# print(f"{nodeA.data}-->{nodeB.data}-->{nodeC.data}-->")


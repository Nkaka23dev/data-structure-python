class Node:
    def __init__(self,data=None,nex=None):
        self.data=data
        self.next=nex

class Linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beggining(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        node=Node(data,nex=None)
        if self.head==None:
            self.head=node
            return 
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=node

    def list_size(self):
        if self.head is None:
            return "The linked List is empty."
        cur=self.head
        counter=0
        while cur!=None:
            counter+=1
            cur=cur.next
        return counter

    def display(self):
        if self.head==None:
            print("The linked list is empty.")
            return 
        cur=self.head
        all_nodes=''
        while cur:
            all_nodes+=str(cur.data)+'---->'
            cur=cur.next
        return all_nodes

    
ll=Linked_list()
ll.insert_at_beggining(12)
ll.insert_at_beggining(67)
ll.insert_at_beggining(23)
ll.insert_at_end(1000)
ll.insert_at_end(657)
ll.insert_at_beggining(1994)
ll.insert_at_beggining(200000)
x=ll.display()
print(x)
print(ll.list_size())

# ll=Linked_list()
# arr=[34,45,7]
# for r in arr:
#     ll.insert_at_beggining(r)

# x=ll.display()
# print(x)























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

# class Node:
#     def __init__(self,data=None,nex=None):
#         self.data=data
#         self.next=nex

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insert_at_beggining(self,data):
#         node=Node(data,self.head)
#         self.head=node

#     def insert_at_end(self,data):
#         node=Node(data,None)
#         if self.head is None:
#             self.head=node
#             return
#         cur=self.head
#         while cur.next is not None:
#             cur=cur.next
#         cur.next=node

#     def display(self):
#         if self.head ==None:
#             print("The linked list is empty.")
#             return
#         cur=self.head
#         all_elem=[]
#         while cur!=None:
#             all_elem.append(cur.data)
#             cur=cur.next
#         print(all_elem)

# ll=LinkedList()
# ll.insert_at_beggining(12)
# ll.insert_at_beggining(34)
# ll.insert_at_end(54)
# ll.insert_at_beggining(-645)
# ll.display()

            
            



        


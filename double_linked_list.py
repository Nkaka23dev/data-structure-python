class Node:
    def __init__(self,data=None,nxt=None,prev=None):
        self.data=data
        self.prev=prev
        self.next=nxt 

class Linked_list:
    def __init__(self):
        self.head=None

    def add_begin(self,data):
        node=Node(data,self.head,None)
        if self.head==None:
            self.head=node
        else:
            self.head.prev=node
            self.head=node
    
    def last_node(self):
        itr=self.head
        while itr.next:
            itr=itr.next

        return itr

    def print_forward(self):
        if self.head==None:
            print("Double linked list is empty.")
            return
        itr=self.head
        container=''
        while itr:
            container+=str(itr.data)+'--->'
            itr=itr.next 
        print(container)

    def print_backward(self):
        if self.head==None:
            print("Linked list is empty.")
            return 

        last_node=self.last_node()
        itr=last_node
        contain=''
        while itr:
            contain+=str(itr.data)+'<---'
            itr=itr.prev
        print(contain)



ll=Linked_list()
ll.add_begin("Nkaka")
ll.add_begin(543)
ll.add_begin("Kanyange")
ll.add_begin("Donatien")
ll.add_begin("Byiringiro")
ll.print_forward()
ll.print_backward()

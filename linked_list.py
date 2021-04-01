class Node:
    def __init__(self,data=None,follow=None):
        self.follow=follow
        self.data=data 

class Linked_list:
    def __init__(self):
        self.head=None 

    def insert_begin(self,data):
        node=Node(data,follow=self.head)
        self.head=node 

    def insert_end(self,data):
        node=Node(data,None)
        if self.head is None:
            self.head=node
            return 
        itr=self.head
        while itr.follow:
            itr=itr.follow
        itr.follow=node
        
    def display(self):
        if self.head is None:
            print("This Linked list is empty.")
            return 
        itr=self.head
        my_list=''
        while itr:
            my_list+=str(itr.data)+'--->'
            itr=itr.follow
        print(my_list) 

    def length(self):
        if self.head==None:
            print("The list is empty.")
            return
        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.follow
        print(count)

   






ll=Linked_list()
ll.insert_end(100)
ll.insert_end(200)
ll.display()
ll.length()

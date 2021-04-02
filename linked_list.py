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

    def extend(self,list_of_elem):
        # self.head=None
        for data in list_of_elem:
            self.insert_end(data)

    def insert_middle(self,index,data):
        if index<0 or index>=self.length():
            raise Exception("Invalid index")
            return
        if index==0:
            self.insert_begin(Node(data))
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.follow)
                itr.follow=node
            count+=1
            itr=itr.follow

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
        return count

    def delete_at(self,index):
        if index<0 or index>=self.length():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.follow
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.follow=itr.follow.follow
                break
            itr=itr.follow
            count+=1

ll=Linked_list()
ll.insert_end(100)
ll.insert_end(200)
ll.insert_begin(23)
ll.extend(["Nkaka","JaneDoe","Amanada","Amina","Kendrick"])
ll.delete_at(3)
ll.insert_middle(2,"I Love you!")
ll.display()
print("The length is: ",ll.length())

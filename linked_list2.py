class Node:
    def __init__(self,data=None,nxt=None):
        self.data=data
        self.next=nxt

class List:
    def __init__(self):
        self.head=None 

    def insert_begin(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_end(self,data):
        node=Node(data,None)
        if self.head==None:
            self.head=node
            return 
        itr=self.head 
        while itr.next:
            itr=itr.next
        itr.next=node 

    def insert_middle(self,index,data):
        if index<0 or index>=self.length():
            print("This Invalid")
        if index==0:
            self.head=Node(data,self.head.next)
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
            count+=1
            itr=itr.next


    def delete(self,index):
        if index<0 or index>=self.length():
            print("Invalid index.")
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def extend(self,many_data):
        for data in many_data:
            self.insert_end(data)

    def clear(self):
        self.head=None
        return

    def length(self):
        if self.head is None:
            raise Exception("Your list is empty!")
            return 

        itr=self.head
        count=0
        while itr:
            count+=1
            itr=itr.next
        return count

    def display(self):
        if self.head==None:
            print("This list is empty.")
            return 
        itr=self.head
        my_list=''
        while itr:
            my_list+=str(itr.data)+'--->'
            itr=itr.next 
        print(my_list)

    

ll=List()
ll.insert_end(56)
ll.insert_end(89)
ll.insert_end(2)
# ll.insert_begin(200)
# ll.insert_begin(234)
# ll.extend(['Nkaka','Christella','Yabebe','Piano'])
# ll.clear()
# ll.delete(1)
ll.insert_middle(0,"Haa")
ll.display()
print("The length of my list is: ",ll.length())


        







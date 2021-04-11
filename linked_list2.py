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
        try:
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
        except Exception as e:
            raise Exception("Error occured",e)
    
    def insert_after_value(self,value_insert_after,data):
        # if self.head==None:
        #     print("The linked list is empty.")
        itr=self.head
        el=[]
        while itr:
            if itr.data==value_insert_after:
                itr.next=Node(data,itr.next)
            el.append(itr.data)
            itr=itr.next
        if value_insert_after not in el and self.length()!=0:
            print("This value does not exist.")

    def remove_by_value(self,data):
        itr=self.head
        counter=0
        while itr:
            if itr.data==data:
                self.delete(counter)
            itr=itr.next
            counter+=1
            
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
            print("Your list is empty!")
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
ll.insert_begin(200)
ll.insert_begin(234)
ll.extend(['Nkaka','Christella','Yabebe','Piano'])
# ll.clear()
# ll.delete(1)
ll.insert_middle(2,"Haa")
ll.insert_after_value("Piano","Victor")
ll.remove_by_value(234)
ll.remove_by_value("Nkaka")
ll.remove_by_value("Haa")
ll.display()
# print("The length of my list is: ",ll.length())


        







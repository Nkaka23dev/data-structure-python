class Node:
    def __init__(self,data,follow):
        self.data=data
        self.next=follow 
    
class LinkedList:
    def __init__(self):
        self.head=None 

    def add_at_beginning(self,data):
        node=Node(data,self.head) 
        self.head=node 

    def print_all_nodes(self): 
        if self.head==None:
            print("The linked list is empty.") 
        itr=self.head 
        all_nodes='' 
        while itr:
            all_nodes+=str(itr.data)+'---->'
            itr=itr.next 
        print(all_nodes) 

    def insert_at_the_end(self,data):
        
    

if __name__=='__main__':
    ll=LinkedList() 
    ll.add_at_beginning(423)
    ll.add_at_beginning(657)
    ll.print_all_nodes() 



    

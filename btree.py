class Binary_tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None 

    def add_child(self,data):
        if data==self.data:
            return 

        if data<self.data:
            if self.left :
                #add data to the left side of the tree   
                self.left.add_child(data)
            else:
                self.left=Binary_tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_tree(data) 

    def in_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements 

    def pre_order_traversal(self):
        elements=[]
        elements.append(self.data)

        if self.left:
            elements+=self.left.in_order_traversal()

        if self.right:
            elements+=self.right.in_order_traversal()

        return elements 
   
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traversal()

        if self.right:
            elements+=self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def search(self,data):
        try:
            if self.data==data:
                return True 
            if data<self.data:
                if self.left:
                    return self.left.search(data)
                else:
                    return False

            else:
                if self.right:
                    return self.right.search(data)
                else:
                    return False
        except Exception as e:
            print("Errors occured.") 

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data 

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data 

    def find_sum_all(self):
        return sum(self.in_order_traversal())

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left=self.left.delete(val)
            else:
                return None
        elif val>self.data:
            if self.right:
                self.right=self.right.delete(val)
            else:
                return None 
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:  
                return self.left

            min_val=self.right.find_min()
            self.data=min_val
            self.right=self.right.delete(min_val)

        return self 
       
def build_tree(elements):
    print("Building tree with he following elements",elements)
    root=Binary_tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    # elements=["Kigali","Kamonyi","Muhanga","Ruhango","Nyaruguru"]
    # elements=[17,4,20,9,23,18,34]
    elements=[100,3,1,4,6,8,9,54,22,45,89,0,23]
    b=build_tree(elements)
    b.delete(22)
    print("In order ",b.in_order_traversal())
    # print(b.search(646))
    # print(b.find_min())
    # print("The max number is: ",b.find_max())
    # print("Sum of all",b.find_sum_all())
    # print("Pre oreder ", b.pre_order_traversal())
    # print("Post oreder ", b.post_order_traversal())




    
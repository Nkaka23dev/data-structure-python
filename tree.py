class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child) 

    
    def calc_level(self):
        start=0
        par=self.parent
        while par:
            start+=1
            par=par.parent
        return start


    def display(self):
        space=' '*self.calc_level()*3
        prifix=space+'|__' if self.parent else""
        print(prifix + self.data)
        if self.children:
            for child in self.children:
                child.display()

  
def build_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("Positivo"))

    TVs=TreeNode("TVs")
    TVs.add_child(TreeNode("TV"))
    TVs.add_child(TreeNode("Samsung"))
    TVs.add_child(TreeNode("LG"))

    cellphones=TreeNode("cellphones")
    cellphones.add_child(TreeNode("Infinix"))
    cellphones.add_child(TreeNode("iphone"))
    cellphones.add_child(TreeNode("Itel"))

    root.add_child(laptop)
    root.add_child(TVs)
    root.add_child(cellphones)

    return root 

    
if __name__=='__main__':
    root=build_tree()
    root.display()
    pass


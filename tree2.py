class TreeNode:
    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        self.children=[]
        self.parent=None 

    def add_child(self,child):
        child.parent=self
        self.children.append(child)

    def display(self,p):
        p=p.casefold()
        spaces=" "*self.get_level()*2
        prefix=spaces+'|__' if self.parent else""
        if p=="name":
            print(f"{prefix} {self.name}")
        elif p=="desi":
            print(f"{prefix} {self.designation}")
        else:
            print(f"{prefix} {self.name} ({self.designation})")
        for child in self.children:
            child.display(p) 

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent 
        return level


def build_tree():
    root=TreeNode("Nilupul","CEO")

     
    Vishwa=TreeNode("Vishwa","Infrastructure Head")

    Vishwa.add_child(TreeNode("Dhaval","Cloud Manager"))
    Vishwa.add_child(TreeNode("Abhijit","App Manager"))

    Aamir=TreeNode("Dhaval","Application head")

    chinmay=TreeNode("Chinmay","CTO")
    chinmay.add_child(Vishwa)
    chinmay.add_child(Aamir)

    gels=TreeNode("Gels","HR Head")
    gels.add_child(TreeNode("Peter","Recruitment Manager"))
    gels.add_child(TreeNode("Waqas","Policy Manager"))
        
    root.add_child(chinmay)
    root.add_child(gels)
    

    return root

# if __name__=='__main__':
#     print("Print by name designation or both")
#     print("Write name,desi or both to print.")
#     p=input("Enter your choice: ")
#     root=build_tree()
#     root.display(p)


'''The following is the second exercice'''

class TreeTwo:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None

    def add_child(self,child):
        child.parent=self
        self.children.append(child) 

    def print_tree(self,level):
        if self.calc_level()>level:
            return 
        spaces=" "*self.calc_level()*2
        prefix=spaces+'|---' if self.parent else""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def calc_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level


def make_tree():
    root=TreeTwo("Global")

    India=TreeTwo("India")

    gujarat=TreeTwo("Gujarat")
    gujarat.add_child(TreeTwo("Ahmedabad"))
    gujarat.add_child(TreeTwo("Baroda"))

    karnataka=TreeTwo("Karnataka")
    karnataka.add_child(TreeTwo("Bangaluru"))
    karnataka.add_child(TreeTwo("Mysore"))

    India.add_child(gujarat)
    India.add_child(karnataka)


    USA=TreeTwo("USA")
    New_Jersey=TreeTwo("New Jersey")
    New_Jersey.add_child(TreeTwo("Princeton"))
    New_Jersey.add_child(TreeTwo("Trenton"))

    Calfornia=TreeTwo("Calfornia")
    Calfornia.add_child(TreeTwo("San Francisco"))
    Calfornia.add_child(TreeTwo("Mountain View"))
    Calfornia.add_child(TreeTwo("Palo Alto"))

    USA.add_child(New_Jersey)
    USA.add_child(Calfornia)

    root.add_child(India)
    root.add_child(USA)

    return root


if __name__=='__main__':
    root=make_tree()
    root.print_tree(3)

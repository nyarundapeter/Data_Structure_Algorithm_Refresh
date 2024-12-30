"""
Extend [tree class] so that it takes **name** and **designation** in data part of TreeNode class.
Now extend print_tree function such that it can print either name tree, designation tree
or name and designation tree.

Here is how your main function should look like,
```
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
```
"""
from tree import TreeNode
from dataclasses import dataclass

@dataclass
class NodeData:
    name:str
    designation: str

class EmployeeNode:
    def __init__(self,data):
        if isinstance(data, NodeData):
            self.data = data
        else:
            raise ValueError("Missing values Name and Designation for node Data")
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, kind:str = "both"):
        spaces = ' ' * self.get_level() * 2
        prefix = spaces + "|-" if self.parent else ""

        if kind == "both":
            print(prefix,self.data.name,"("+self.data.designation+")")
        elif kind == "name":
            print(prefix, self.data.name)
        elif kind == "designation":
            print(prefix, self.data.designation)
        if self.children:
            for child in self.children:
                child.print_tree(kind)

def build_management_tree():

    management_tree = TreeNode("Management Tree")

    ceo=EmployeeNode(NodeData("Zennix","CEO"))
    management_tree.add_child(ceo)

    # CTO Branch
    cto = EmployeeNode(NodeData("Thalira","CTO"))
    ceo.add_child(cto)
    infrahead = EmployeeNode(NodeData("Ryven", "Infrastructure Head"))
    cto.add_child(infrahead)
    cloud_manager = EmployeeNode(NodeData("Maelis","Cloud Manager"))
    infrahead.add_child(cloud_manager)
    app_manager = EmployeeNode(NodeData("Jyxon","App Manager"))
    infrahead.add_child(app_manager)
    app_head = EmployeeNode(NodeData("Astrild","Application Head"))
    cto.add_child(app_head)

    # HR Branch Nyxis Vyndor
    hr = EmployeeNode(NodeData("Kaelum","HR"))
    ceo.add_child(hr)
    recruit_manager = EmployeeNode(NodeData("Nyxis", "Recruitment Manager"))
    hr.add_child(recruit_manager)
    policy_manager = EmployeeNode(NodeData("Waqas", "Policy Manager"))
    hr.add_child(policy_manager)

    return ceo

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree()
    print("\n ________________")
    root_node.print_tree("name")
    print("\n ________________")
    root_node.print_tree("designation")





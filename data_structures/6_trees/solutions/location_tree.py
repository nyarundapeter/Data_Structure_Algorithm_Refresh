"""
Build a location tree using TreeNode class
Modify print_tree method to take tree level as input.
And that should print tree only upto that level.
"""

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)


    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, level: int):
        #print(level, self.get_level())
        if(self.get_level()<=level):
            spaces = ' ' * self.get_level() * 2
            prefix = spaces + "|-" if self.parent else ""
            print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(level)



def build_location_tree():
    location = TreeNode("Global")

    africa = TreeNode("Africa")
    location.add_child(africa)


    kenya = TreeNode("Kenya")
    nairobi = TreeNode("Nairobi")
    nyanza = TreeNode("Nyanza")
    africa.add_child(kenya)
    kenya.add_child(nairobi)
    nairobi.add_child(TreeNode("Westlands"))
    nairobi.add_child(TreeNode("Eastlands"))
    kenya.add_child(nyanza)
    nyanza.add_child(TreeNode("Kisumu"))
    nyanza.add_child(TreeNode("Kisii"))

    sa = TreeNode("South Africa")
    africa.add_child(sa)
    gauteng=TreeNode("Gauteng")
    cape=TreeNode("Western Cape")
    gauteng.add_child(TreeNode("Johannesburg"))
    gauteng.add_child(TreeNode("Pretoria"))
    sa.add_child(gauteng)
    sa.add_child(cape)

    return location


if __name__ == "__main__":
    root = build_location_tree()
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)
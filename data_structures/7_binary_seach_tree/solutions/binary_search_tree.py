class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data== val:
            return True

        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # find_min(): finds minimum element in entire binary tree
    def find_min(self):

        if self.left is None:
           min = self.data
        else:
            min = self.left.find_min()
        return min

    # find_max(): finds maximum element in entire binary tree
    def find_max(self):

        if self.right is None:
           max = self.data
        else:
            max = self.right.find_max()
        return max

    # calculate_sum(): calculates sum of all elements
    def calculate_sum(self):
        sum = 0
        for elements in self.in_order_traversal():
            sum += elements
        return sum

    # post_order_traversal(): performs post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    # pre_order_traversal(): perofrms pre order traversal of a binary tree
    def pre_order_traversal(self):

        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range (1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    #numbers = [17]
    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())
    #print(numbers_tree.search(20))
    #print("Min of Binary Tree is: ",numbers_tree.find_min())
    #print("Max of Binary Tree is: ",numbers_tree.find_max())
    #print(numbers_tree.calculate_sum())
    #print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())

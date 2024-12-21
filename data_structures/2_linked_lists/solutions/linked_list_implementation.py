class Node:
    """
    Initializes a new instance of the Node class.

    Args:
        data: The value or data to be stored in the node. Defaults to None.
        next: A reference to the next node in the linked list. Defaults to None.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head: A reference (pointer) to the first node in the linked list.
              Defaults to None, indicating an empty list.
    """
    def __init__(self):
        self.head = None



    def insert_at_begining(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Args:
            data: The value or data to be stored in the new node.

        Steps:
            1. Create a new node with the given data and set its next pointer to the current head.
            2. Update the head of the linked list to point to the new node.

        This operation effectively makes the new node the first element of the linked list.
        """
        node = Node(data, self.head)
        self.head = node



    def print(self):
        """
        Prints the elements of the linked list in a readable format.

        Steps:
            1. Check if the linked list is empty (head is None).
               If it is, print a message indicating the list is empty and return.
            2. If the list is not empty, iterate through each node starting from the head.
            3. Append each node's data to a string, separated by '-->' to represent links between nodes.
            4. After traversal, print the final string representation of the linked list.

        Example Output:
            For a linked list with elements 3 -> 7 -> 9, it will print: "3-->7-->9-->"
        """
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data: The value or data to be stored in the new node.

        Steps:
            1. Check if the linked list is empty (head is None).
               - If empty, create a new node and set it as the head of the list.
               - Return after the insertion since there's no more processing required.
            2. If the list is not empty:
               - Start at the head and traverse through the linked list until the last node.
               - Once at the last node (where next is None), create a new node and set it as the next node.

        This operation effectively adds the new node to the end of the linked list.
        """
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """
        Replaces the current linked list with nodes created from a list of values.

        Args:
            data_list: A list of values to be inserted into the linked list.

        Steps:
            1. Set the head of the linked list to None, effectively clearing any existing nodes.
            2. Iterate through each value in the given list.
            3. For each value, call the `insert_at_end` method to add it as a new node at the end of the linked list.

        This method allows you to bulk-insert values into the linked list, starting with an empty list.
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Calculates and returns the total number of nodes in the linked list.

        Steps:
            1. Initialize a counter variable to 0.
            2. Start iterating from the head of the linked list.
            3. For each node encountered, increment the counter by 1.
            4. Continue the iteration until reaching the end of the list (where the node's `next` is None).
            5. Return the final counter value as the length of the linked list.

        Returns:
            int: The total number of nodes in the linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        """
       Removes the node at the specified index from the linked list.

       Args:
           index: The position (0-based) of the node to be removed.

       Steps:
           1. Validate the index:
              - If the index is negative or greater than/equal to the length of the list, raise an exception.
           2. Handle the case where the index is 0:
              - Update the head to point to the second node, effectively removing the first node.
           3. For other indices:
              - Start from the head and iterate through the list to find the node at (index - 1).
              - Update the `next` pointer of this node to skip the node at the specified index, effectively removing it.
           4. Stop the iteration once the removal is done.

       Raises:
           Exception: If the provided index is invalid.

       Example:
           For a linked list with elements 10 -> 20 -> 30 -> 40, calling `remove_at(2)` will make the list 10 -> 20 -> 40.
       """
        if index<0 or index>=self.get_length():
           raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count += 1

    def insert_at(self, index, data):
        """
        Inserts a new node with the given data at the specified index in the linked list.

        Args:
            index: The 0-based position where the new node is to be inserted.
            data: The value or data to be stored in the new node.

        Steps:
            1. Validate the index:
               - Raise an exception if the index is negative or greater than/equal to the length of the list.
            2. Handle the case where the index is 0:
               - Call the `insert_at_begining` method to insert a new node at the start of the list.
            3. For other indices:
               - Traverse the list to find the node at (index - 1).
               - Create a new node whose `next` pointer points to the current node at the specified index.
               - Update the `next` pointer of the (index - 1) node to point to the new node.
            4. Stop the iteration once the insertion is done.

        Raises:
            Exception: If the index is invalid.

        Example:
            For a linked list with elements 10 -> 20 -> 40:
            Calling `insert_at(2, 30)` will result in 10 -> 20 -> 30 -> 40.
        """
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr=itr.next
            count += 1


    """
    Q1 : def insert_after_value(self, data_after, data_to_insert):
             Search for first occurance of data_after value in linked list
             Now insert data_to_insert after data_after node
    """
    def insert_after_value(self, data_after, data_to_insert):
        """
        Inserts a new node with the value `data_to_insert` immediately after the first occurrence
        of a node containing the value `data_after` in the linked list.

        Args:
            data_after: The value in the linked list after which the new node should be inserted.
            data_to_insert: The value to be inserted into the new node.

        Steps:
            1. Check if the linked list is empty:
               - If `self.head` is `None`, raise an exception indicating that the linked list is empty.
            2. Traverse the linked list:
               - Start at the head node and iterate through the linked list using a `while` loop.
               - At each node, check if the `data` matches `data_after`.
            3. Insert the new node:
               - If a match is found, create a new node with value `data_to_insert`.
               - Set the `next` pointer of the new node to point to the `next` node of the matched node.
               - Update the `next` pointer of the matched node to point to the new node.
               - Break out of the loop after inserting the node.
            4. Handle the case where `data_after` is not found:
               - If the loop completes and no matching node is found, raise an exception indicating that
                 the value `data_after` does not exist in the linked list.

        Raises:
            Exception: If the linked list is empty or if the value `data_after` is not found in the list.

        Example:
            For a linked list containing 10 -> 20 -> 30:
            Calling `insert_after_value(20, 25)` will modify the list to 10 -> 20 -> 25 -> 30.
        """
        if self.head is None:
            raise Exception("Linked List is empty")

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next
        else:
            raise Exception("Data after which to insert is not found")

    """
    Q2 : def remove_by_value(self, data):
    # Remove first node that contains data
    """
    def remove_by_value(self, data):
        """
        Removes the first node in the linked list that contains the specified value.

        Args:
            data: The value of the node to be removed.

        Raises:
            Exception: If the linked list is empty or if the data is not found in the list.

        Steps:
            1. Check if the linked list is empty.
            2. If the head node contains the target value, update the head pointer to skip the head node.
            3. Traverse the list to find the first node containing the target value.
            4. Remove the node by adjusting the previous node's `next` pointer to skip the matched node.
            5. If the value is not found after traversal, raise an exception.
        """
        if self.head is None:
            raise Exception("Linked List is empty")

        itr = self.head
        while itr:
            if self.head.data == data:
                self.head = self.head.next
                break
            if itr.data == data:
                if itr.next is None:
                    itr.next = None
                    break
                itr.next = itr.next.next
                break
            itr = itr.next

        else:
            raise Exception("Data not found")

if __name__ == '__main__':
    """
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(79)
    ll.print()
    
    ll2 = LinkedList()
    ll2.insert_values(["banana", "mango", "grapes", "orange"])
    ll2.print()
    print(f"Length of Linked list: {ll2.get_length()}")
    ll2.remove_at(2)
    ll2.print()
    ll2.insert_at(0, "figs")
    ll2.insert_at(2, "jackfruit")
    ll2.print()
    """


    """
    Exercise Execution
    """
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()

    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    # ll.remove_by_value("figs")
    # Runs into a "Data not found error as it is not part of the linked list" thus commented out
    #ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
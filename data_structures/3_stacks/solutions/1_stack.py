import copy
from collections import deque


class Stack:
    def __init__(self):
        """
        Initialize an empty stack using a deque container.
        """
        self.container = deque()

    def push(self, val):
        """
        Add the given value to the top of the stack.

        Args:
            val: The value to be added to the stack.
        """
        self.container.append(val)

    def pop(self):
        """
       Remove and return the value at the top of the stack.

       Returns:
           The value removed from the top of the stack.
       """
        return self.container.pop()

    def peek(self):
        """
        Return the value at the top of the stack without removing it.

        Returns:
            The value at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.container[-1]

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.container) == 0

    def size(self):
        """
        Get the number of elements in the stack.

        Returns:
            The size of the stack.
        """
        return len(self.container)

    def print_stack(self):
        """
        Print each element in the stack.
        """
        for s_item in self.container:
            print(f"{s_item}")

    """
    Q1: Write a function in python that can reverse a string using stack data structure. 
    reverse_string("We will conquer COVID-19") should return "91-DIVOC reuqnoc lliw eW"
    """
    def reverse(self):
        """
        Create a new stack with elements reversed from the original stack.

        Returns:
            A new Stack object with the elements in reverse order.
        """
        reversed_stack = Stack()
        duplicate_stack = copy.deepcopy(self)
        count = self.size()
        itr = 0
        while itr < count:
            reversed_stack.push(duplicate_stack.pop())
            itr += 1
        return reversed_stack

"""
Q2: Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". 

is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""
def is_balanced(string):
    """
    Check if the parentheses in the given string are balanced.

    Args:
        string: The input string containing parentheses to be checked.

    Returns:
        True if the parentheses are balanced, False otherwise.
    """
    stack = Stack()
    string = string
    input_brace = ["(", "{", "["]
    output_brace = [")", "}", "]"]
    for s_character in string:
        if s_character in input_brace:
            stack.push(s_character)
        if s_character in output_brace:
            if stack.is_empty():
                # print(f"Stack is empty yet we have closing {character}")
                return False
            stack.pop()

    return stack.is_empty()



if __name__ == '__main__':
    s = Stack()

    string_to_be_reversed = "We will conquer COVID-19"

    for character in string_to_be_reversed:
        s.push(character)
    rs = s.reverse()
    reversed_string = ""

    for item in rs.container:
        reversed_string += item

    print(reversed_string)

    print("\n",
        is_balanced("({a+b})"),"\n", # True
        is_balanced("))((a+b}{"),"\n", # False
        is_balanced("((a+b))"),"\n", # True
        is_balanced("))"),"\n", # False
        is_balanced("[a+b]*(x+2y)*{gg+kk}") # True
    )
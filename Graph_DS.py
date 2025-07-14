#A basic graph 
from collections import deque

class graph:
    def __init__(self):
        self.root = None

    def populate_treee(nodes):
        for individual in nodes:
            individual = node()


class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# binary tree where root is always middle value
class binary_tree():
    def __init__(self):
        self.root = None

    def create_tree(self, input_list):
        if not input_list:
            return

        input_list = list(input_list)
        input_list.sort()  

        middle_index = len(input_list) // 2
        root_value = input_list[middle_index]
        self.root = node(root_value)

        for i, val in enumerate(input_list):
            if i == middle_index:
                continue  
            self.insert(val)

    def insert(self, value):
        new_node = node(value)
        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right

def main():
    bin_tree = binary_tree()
    num_list = deque([15, 10, 5, 0])
    bin_tree.create_tree(num_list)

if __name__ == "__main__":
    main()
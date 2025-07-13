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

#binary tree with structured where root is always middle value. 
class binary_tree():
    def __init__(self):
        self.root = None
        self.current_node = None

    def create_tree(self,input_list):
        input_list.sort()
        left_list = []
        right_list = []
        middle = len(input_list)//2
        for _ in range(middle):
             if len(input_list) == 1:
                self.root = node(input_list.pop())
             left_list.append(input_list.pop())
             right_list.append(input_list.deque.popleft())
        if self.root == None:
            self.root = node((left_list[-1] + left_list[-1]) // 2)
        for _ in range(middle):
            #From the root left and right should be connected to right_list[-1] and left_list[-1] since
            #that will be the highest value, after that make sure all values are properly linked to eachother. 
            pass


def main():
    graphing = graph()
    bin = binary_tree()
    #the binary tree takes where values split from smallest to biggest 

    num_list = deque([15,10,5,0])
    graphing.populate_treee(len(num_list))

if __name__ == "__main__":
    main()
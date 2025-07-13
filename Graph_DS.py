#A basic graph 


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


class binary_tree():
    def __init__(self):
        self.root = None
        self.current_node = None

    def create_tree(self,input_list):
        input_list.sort()
        middle = len(input_list)//2
        
        self.root = input_list.pop()
        self.root = node(value)
        for value in input_list:
            current_node = node(value)



def main():
    graphing = graph()
    bin = binary_tree()
    #the binary tree takes where values split from smallest to biggest 

    num_list = [15,10,5,0]
    graphing.populate_treee(len(num_list))

if __name__ == "__main__":
    main()
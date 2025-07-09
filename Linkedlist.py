import random

class linkedlist(object):
    def __init__(self, r = None):
        self.root = r 
        self.size = 0 

    def get_size(self):
        return self.size
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1 
        return new_node
   

class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n 

    def get_data(self):
        return self.data
    
    def set_data(self, d):
        self.data = d

def main():
    llist = linkedlist()
    Amount_of_nodes = input("Amount of nodes to add -> ")

    if Amount_of_nodes.isdigit():
        Amount_of_nodes = int(Amount_of_nodes)
        for curr_loop in range (Amount_of_nodes):
            current_node_value = input(f'{curr_loop} Add a value > ')
            currentnode = llist.add(current_node_value)


    node_value_list = []
    while currentnode is not None:
        node_value_list.append(currentnode.get_data())
        currentnode = currentnode.next_node
    print(f'->'.join(node_value_list))
if __name__ == '__main__':
    main()
class Node(object): #Binary tree implementation from https://www.tutorialspoint.com/python/python_binary_tree.htm
    def __init__(self, data):
        self.data = data
        self.left = left
        self.right = right

#Serialize the binary tree
def serialize(self, root):
    self.vals = [] # Empty list to append each node value
    def tree2string(node):
        if node:
            #Append node value and recursively call the function to continue down the tree
            self.vals.append(str(node.val)) 
            tree2string(node.left) #Left values traversed first
            tree2string(node.right)
        else:
            #If it is not a node, append a placeholder that shouldn't be the value of any node
            self.vals.append('@')
    tree2string(root)
    return ' '.join(self.vals) #Turn the array into a string

#Deserialize the string
def deserialize(self, data):
    def string2tree(vals):
        val = next(vals) #Comparing each value of the string to see if it is a terminating node
        if val == '@':
            return None #If not a node, return value as None

        node = Node(int(val))
        node.left = string2tree(vals) #If it is not, set the value of our node to be this value and recursively run string2tree for the left and right values.
        node.right = string2tree(vals) #Because we traversed the left values first we must also put them back first

        return node
    vals = iter(data.split()) #split the data into an array from a string
    return string2tree(vals) 

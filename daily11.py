class Node:
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next_node
    def set_next(self):
        self.next_node = new_next



class LinkedList:
    def __init__(self, head=None):
        self.head = head

list1 = LinkedList()
list1.head= Node(3)
val1 = Node(7)
val2 = Node(8)
val3 = Node(10)
list1.head.next_node = val1
val1.next_node = val2
val2.next_node = val3

list2 = LinkedList()
list2.head= Node(99)
vval1 = Node(1)
vval2 = Node(8)
vval3 = Node(10)
list2.head.next_node = vval1
vval1.next_node = vval2
vval2.next_node = vval3

def traverse(self1,self2):
        node1 = self1.head
        node2 = self2.head
        i=0
        while node1 and node2 != None:
            if node1.data == node2.data:
                return i
            else:
                i=i+1
                node1=node1.next_node
                node2=node2.next_node


print(traverse(list1,list2))

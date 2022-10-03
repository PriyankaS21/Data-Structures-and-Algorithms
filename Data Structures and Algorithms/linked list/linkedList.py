class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insertat(self, prev_node, new_value):
        if prev_node is None:
            print("prev node seems to be empty")

        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_value):
        new_value = Node(new_value)
        if self.head is None:
            self.head = new_value
            return
        
        last = self.head
        while(last.next):
            last = last.next
        
        last.next = new_value

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(3)
    llist.push(4)
    llist.printlist()


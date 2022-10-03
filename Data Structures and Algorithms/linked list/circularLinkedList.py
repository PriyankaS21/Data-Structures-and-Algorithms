class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head

        new_node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def tocircular(self, head):
        start = head

        while(head.next is not None):
            head = head.next
        
        head.next = start
        return start

    def delete(self, deleteval):
        current_node = self.head
        prev_node = None

        while current_node:

            if current_node.data == deleteval and current_node == self.head:
                # Case 1, head is only element in the C list
                if current_node.next == self.head:
                    current_node = None
                    self.head = None
                
                # Case 2, There are more element in the C list
                else:
                    # traverse and update head: delete head
                    while current_node.next != self.head:
                        current_node = current_node.next
                    current_node.next = self.head
                    self.head = self.head.next
                    current_node = None
                    return
            elif current_node == deleteval:
                prev_node.next = current_node.next
                current_node = None
                return                
            else:
                if current_node.next == self.head:
                    break
            prev_node = current_node
            current_node = current_node.next

    def countnodes(self):
        current = self.head
        self.count = 1
        while(current.next != self.head):
            self.count = self.count + 1
            current = current.next
        print("Count: ",self.count)

    def printCLinkedList(self):
        temp = self.head
        if self.head is not None:
            while(True):
                print(temp.data)
                temp = temp.next
                if (temp == self.head):
                    break


myClist = CircularLinkedList()
myClist.push(5)
myClist.push(6)
myClist.push(10)
myClist.printCLinkedList()
myClist.countnodes()
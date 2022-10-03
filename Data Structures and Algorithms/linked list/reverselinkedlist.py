class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value) #new node is created but it is not a part of linked list yet
        new_node.next = self.head # Here whatsever head is pointing out, now we making head to point to next node, which is created just now, 
                                # and since the head wad pointing to null, so we make next node pointing to null(head)
        self.head = new_node # redirect head to pointing to new node

    def insertat(self, prev_node, new_value, lb, ub):
        if prev_node is None:
            print("prev node seems to be empty")

        new_node = Node(new_value)  
        # new_node.next = prev_node.next
        # prev_node.next = new_node

        temp = self.head
        if self.head == lb: # handle the case for insert at 2nd pos
            new_node.next = temp.next
            temp.next = new_node

        while (temp.next):            
            temp = temp.next
            if temp.data == lb:
                new_node.next = temp.next
                temp.next = new_node

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

    def deleteNode(self, key):
        
        temp = self.head

        # Case 1
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Case 2
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # Case 3
        if (temp == None):
            return

        prev.next = temp.next
        temp = None
    
    def deletetotallist(self):
        curr = self.head
        while curr:
            prev = curr.next

            del curr.data

            curr = prev

    
    def getnodecount(self, node):
        if (not node):
            return 0
        else:            
            return 1 + self.getnodecount(node.next)
        # c = 0        
        # while(node.next):            
        #     if (not node):
        #         break
        #     else:
        #         c += 1

        # return c 

    def getcount(self):
        return self.getnodecount(self.head)

    def linkedreverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    


if __name__ == '__main__':
    llist = LinkedList() # head is created and pointing to None
    llist.append(3)
    # llist.push(4)      
    llist.append(5)
    llist.append(7)
    llist.append(6) 
    llist.append(8)
    llist.insertat(llist.head.next,1,5,8)
    llist.printlist()
    print('Count',llist.getcount())
    llist.linkedreverse()
    llist.printlist()


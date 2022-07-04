class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def push(self,ele):
        if not self.head:
            self.head = Node(ele)
            return
        newNode = Node(ele)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return
        
        popped = self.head
        self.head = self.head.next
        popped.next = None

    def print_elements(self):
        temp = self.head

        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("\n")

ll = LinkedList()
ll.push(10)
ll.push(9)
ll.push(8)
ll.push(7)

ll.print_elements()

ll.pop()

ll.print_elements()
ll.pop()

ll.print_elements()

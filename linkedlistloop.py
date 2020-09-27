# Node class 
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None

      # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

    def detectLoopMethod1(self):
        # using a hash set
        s = set()
        temp = self.head
        while(temp != None):
            if temp in s:
                return True
            s.add(temp)
        return False

    def detectLoopMethod2(self):
        # using a pointers
        slow = self.head
        fast = self.head

        # Check for fast.next as it would be the first one to reach the end
        while (slow != None and fast != None and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    def reverse_a_linked_list(self):
        if self.head == None:
            return
        
        after = None
        prev = None
        curr = self.head

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        self.head = prev

        self.printList()
        return

    def middle_elem(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        print(slow.data)



       
# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(20)
 
# Create a loop for testing
#llist.head.next.next.next.next = llist.head
if(llist.detectLoopMethod2()):
        print "Found Loop"
else:
        print "No Loop"
#llist.printList()
print("\n")
#llist.reverse_a_linked_list()
llist.middle_elem()


import collections

class newNode:  
    # Constructor to create a newNode  
    def __init__(self, data):  
        self.data = data  
        self.left = None
        self.right = None

def level_order(root):

    if root == None:
        return

    curret_queue =  collections.deque()

    curret_queue.append(root)

    while len(curret_queue) > 0:
        temp = curret_queue.popleft()
        print(temp.data)

        if temp.right != None:
            curret_queue.append(temp.right)
        if temp.left != None:
            curret_queue.append(temp.left)

def inorder(root):

    if root:
        inorder(root.left)
        print (root.data)
        inorder(root.right)

def height(root):
    if root == None:
        return 0
    
    ltree = height(root.left)
    rtree = height(root.right)
    if ltree > rtree:
        return ltree + 1
    else:
        return rtree + 1
    


if __name__ == '__main__': 
    root = newNode(0)  
    root.left = newNode(1)  
    root.left.left = newNode(3)  
    root.left.left.left = newNode(7)  
    root.left.right = newNode(4)  
    root.left.right.left = newNode(8)  
    root.left.right.right = newNode(9)  
    root.right = newNode(2)  
    root.right.left = newNode(5)  
    root.right.right = newNode(6)  

    #level_order(root)
    #height_of_tree = height(root)
    #print(height_of_tree)
    inorder(root)

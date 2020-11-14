class Node:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def print_path(root):
  rightpath = []
  leftpath = []
  if not root:
    return []
  if not root.right and not root.left:
    return [root.val]
  elif root.right:
    rightpath = [root.val] + print_path(root.right)
  elif root.left:
    leftpath = [root.val] + print_path(root.left)
  return rightpath if len(rightpath) > len(leftpath) else leftpath
  
def how_deep(root):
    # fill in
    # This thing is failing and I honestly dont know why .... :(
    right_path = []
    left_path = []
    if not root:
        return []
    if not root.right and not root.left:
        return [root.val]
    elif root.right is not None:
        right_path = [root.val] + how_deep(root.right)
    elif root.left is not None:
        print(root.left.val)
        left_path = [root.val] + how_deep(root.left)
  	
    left = len(left_path)
    right = len(right_path)
    print(left)
    print(right)


root_node = Node('a')
root_node.left = Node('b')
root_node.left.left = Node('c')
root_node.left.left.left = Node('f')

print print_path(root_node)
how_deep(root_node)
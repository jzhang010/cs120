#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    if v is None: 
      return 0
    else: 
      v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r): 
    n = r.size
    cur = r
    while (cur.left and cur.left.size > n/2) or (cur.right and cur.right.size > n/2):
      if cur.left and cur.left.size > n/2:
        cur = cur.left
      else:
        cur = cur.right
    return cur


      



# A binary tree class.
class Tree:

    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    # def __repr__(self, level=0, indent="    "):
    #     s = level*indent + repr(self.label)
    #     if self.left:
    #         s = s + "\\n" + self.left.__repr__(level+1, indent)
    #     if self.right:
    #         s = s + "\\n" + self.right.__repr__(level+1, indent)
    #     return s

    def __iter__(self):
        return inorder(self)
# Create a Tree from a list.
def tree(list):
    n = len(list)
    if n == 0:
        return []
    i = n // 2
    return Tree(list[i], tree(list[:i]), tree(list[i+1:]))
# Show it off: create a tree.
#t = tree("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# A recursive generator that generates Tree labels in in-order.

l,m,r = 0,0,0
# def inorder(t):
#     global l,m,r
#     if t:
#         for x in inorder(t.left):
#             l += 1
#             print("\nleft tree is yield number: ",l)
#             yield x
#         m += 1
#         print("\nroot is yield number: ",m)
#         yield t.label
#         for x in inorder(t.right):
#             r += 1
#             print("\nright tree is yield number: ",r)
#             yield x
# Show it off: create a tree.
tr = tree("bac")

# it = iter(t)
# print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

def inorder(t):
    stack = []
    tmp  = t
    stack.append(tmp)

    while stack:
        
        while tmp.left:
            stack.append(tmp.left)
            tmp = tmp.left

        tmp = stack.pop()
        yield tmp.label

        while not tmp.right:
            stack.append(tmp.right)
            tmp = tmp.right
        
        


# Print the nodes of the tree in in-order.
# for x in tr:
#     print(' '+x, end='')

# A non-recursive generator.
def inorder(node):
    stack = []
    while node:
        while node.left:
            stack.append(node)
            node = node.left
        yield node.label
        while not node.right:
            try:
                node = stack.pop()
            except IndexError:
                return
            yield node.label
        node = node.right
# Exercise the non-recursive generator.
for x in tr:
    print(' '+x, end='')


import sys

lis = []

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class BinarySearchTree:

    def __init__(self):
            self.root = None
            self.size = 0

    
    #converted from lecture book pseudocode
    def insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    #converted from lecture book pseudocode
    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    #converted from lecture book pseudocode
    def remove(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    #converted from lecture book pseudocode
    def search(self, x, k):
        if x == None or k.key == x.key:
            return x
        if k.key < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    #converted from lecture book pseudocode
    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    #converted from lecture book pseudocode
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    #converted from lecture slide pseudocode
    def to_list_preorder(self, x):
        if x != None:
            lis.append(str(x.key))
            self.to_list_preorder(x.left)
            self.to_list_preorder(x.right)
        return lis

    #converted from lecture slide pseudocode
    def to_list_inorder(self, x):
        if x != None:
            self.to_list_inorder(x.left)
            lis.append(str(x.key))
            self.to_list_inorder(x.right)
        return lis
        
    #converted from lecture slide pseudocode
    def to_list_postorder(self, x):
        if x != None:
            self.to_list_postorder(x.left)
            self.to_list_postorder(x.right)
            lis.append(str(x.key))
        return lis
    




def driver():
    bst = BinarySearchTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if len(in_data) > 1:
                nod = Node(int(value_option[0]))


            if action == "max":
                root = bst.root
                if root == None:
                    print("Empty") 
                else:
                    m = bst.maximum(root)
                    print(m.key)

            elif action == "min":
                root = bst.root
                if root == None:
                    print("Empty") 
                else:
                    m = bst.minimum(root)
                    print(m.key) #print the value of the node, not the node itself
                
            elif action == "insert":
                bst.insert(nod)

            elif action == "remove":
                if bst.search(bst.root, nod) == None:
                   print("TreeError")
                    
                else:
                    nod = bst.search(bst.root, nod)
                    bst.remove(nod)

            elif action == "search":
                if bst.search(bst.root, nod) != None:
                    print("Found")
                
                else:
                    print("NotFound")

            elif action == "inprint":
                root = bst.root
                if root == None:
                    print("Empty") 
                else:
                    l = bst.to_list_inorder(root)
                    print(' '.join(l)) #formatted to print the correct way as specified
                



            elif action == "preprint":
                root = bst.root
                if root == None:
                    print("Empty")
                else:
                    l = bst.to_list_preorder(root)
                    print(' '.join(l)) #formatted to print the correct way as specified
                

            elif action == "postprint":
                root = bst.root
                if root == None:
                    print("Empty") 
                else:
                    l = bst.to_list_postorder(root)
                    print(' '.join(l)) #formatted to print the correct way as specified
            
            del lis[:] #I used .clear() but after testing on ix-dev, the clear method did not work so I found this online at Stack Overflow: https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists




if __name__ == "__main__":
    driver()
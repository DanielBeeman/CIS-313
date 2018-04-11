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

    
    #converted from  book pseudocode
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

    #converted from book pseudocode
    def transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    #converted from book pseudocode
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

    #converted from book pseudocode
    def search(self, x, k):
        if x == None or k.key == x.key:
            return x
        if k.key < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    #converted from book pseudocode, we only need this to help with our remove function.
    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x
    
    #Andy gave us the pseudocode for this in lab, I just converted it. The use of a helper function is so that we can pass the root into a functin, because the documentation
    #did not let us pass anything into the function; the auxiliary function allows us to do each root-node traversal. 
    def best_path_value(self):
        return self.bpv_help(self.root)

        

    def bpv_help(self, x):
        if x == None:
            return 0
        left = self.bpv_help(x.left)
        right = self.bpv_help(x.right)
        return max(left,right) + str(x.key).count('5') #This is at the heart of our helper function: it checks the number of 5's for a given path, and returns the maximum.

                



def driver():
    bst = BinarySearchTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if len(in_data) > 1:
                nod = Node(int(value_option[0]))

            if action == "min":
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

            elif action == "bpv":
                root = bst.root
                if root == None:
                    print("TreeError")
                else:
                    print(bst.best_path_value())

            
            del lis[:] #I used .clear() but after testing on ix-dev, the clear method did not work so I found this online at Stack Overflow: https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists



if __name__ == "__main__":
    driver()
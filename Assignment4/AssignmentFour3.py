import sys
sys.setrecursionlimit(10000000)

lis = [] #The list that'll do the inorder walk and print it out.

class Node:
    def __init__(self, key, color, value):
        self.key = key
        self.color = color
        self.left = value
        self.right = value
        self.p = value
        


class RedBlackTree:

    def __init__(self):
            self.root = sent
            self.size = 0

    
    #converted from book pseudocode
    def insert(self, z):
        y = sent
        x = self.root
        while x != sent:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == sent:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = sent
        z.right = sent
        z.color = "RED"
        self.RB_Insert_Fixup(z)




    #converted from book pseudocode
    def transplant(self, u, v):
        if u.p == sent:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != sent:
            v.p = u.p

    #converted from book pseudocode
    def remove(self, z):
        if z.left == sent:
            self.transplant(z, z.right)
        elif z.right == sent:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.p != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y

    #converted from book pseudocode
    def search(self, x, k):
        if x == sent or k.key == x.key:
            return x
        if k.key < x.key:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    #converted from book pseudocode
    def tree_maximum(self, x):
        while x.right != sent:
            x = x.right
        return x

    #converted from book pseudocode
    def tree_minimum(self, x):
        while x.left != sent:
            x = x.left
        return x


    #converted from book pseudocode
    def to_list_inorder(self, x):
        if x != sent:
            self.to_list_inorder(x.left)
            lis.append(str(x.key))
            self.to_list_inorder(x.right)
        return lis



    #converted from book pseudocode
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != sent:
            y.left.p = x
        y.p = x.p
        if x.p == sent:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    #converted from book pseudocode
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != sent:
            y.right.p = x
        y.p = x.p
        if x.p == sent:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.right = x
        x.p = y


    #converted from book pseudocode
    def RB_Insert_Fixup(self, z):
        while z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.right_rotate(z.p.p)
            elif z.p == z.p.p.right:
                y = z.p.p.left 
                if y.color == "RED":
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = "BLACK"
                    z.p.p.color = "RED"
                    self.left_rotate(z.p.p)
        self.root.color = "BLACK"

    #converted from book pseudocode
    def rb_transplant(self, u, v):
        if u.p == sent:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    #converted from book pseudocode
    def rb_delete(self, z):
        y = z
        y_og_c = y.color
        if z.left == sent:
            x = z.right
            self.rb_transplant(z, z.right)
        elif z.right == sent:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            y_og_c = y.color
            x = y.right
            if y.p == z:
                x.p = y 
            else:
                self.rb_transplant(y, y.right)
                y.right = z.right 
                y.right.p = y 
            self.rb_transplant(z, y)
            y.left = z.left 
            y.left.p = y 
            y.color = z.color
        if y_og_c == "BLACK":
            self.rb_delete_fixup(x)

    #converted from book pseudocode
    def rb_delete_fixup(self, x):
        while x != sent and x.color == "BLACK":
            if x == x.p.left:
                w = x.p.right 
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.left_rotate(x.p)
                    w = x.p.right 
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.p 
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.right_rotate(w)
                        w = x.p.right 
                    w.color = x.p.color
                    x.p.color = "BLACK"
                    w.right.color = "BLACK"
                    self.left_rotate(x.p) 
                    x = self.root
            else:
                w = x.p.left 
                if w.color == "RED":
                    w.color = "BLACK"
                    x.p.color = "RED"
                    self.right_rotate(x.p)
                    w = x.p.left 
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.p 
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.left_rotate(w)
                        w = x.p.left 
                    w.color = x.p.color
                    x.p.color = "BLACK"
                    w.left.color = "BLACK"
                    self.right_rotate(x.p) 
                    x = self.root

    

#my sentinel node, with key value of none, color as black (property of red-black trees), and value of none. 
sent = Node(None, "BLACK", None)

def driver():
    rbt = RedBlackTree()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if len(in_data) > 1:
                nod = Node(int(value_option[0]), "RED", sent) #This allows the creation of all nodes that are not the sentinel 


            if action == "max":
                root = rbt.root
                if root == sent:
                    print("Empty") 
                else:
                    m = rbt.tree_maximum(root)
                    print(m.key)

            elif action == "min":
                root = rbt.root
                if root == sent:
                    print("Empty") 
                else:
                    m = rbt.tree_minimum(root)
                    print(m.key) #print the value of the node, not the node itself
                
            elif action == "insert":
                rbt.insert(nod)

            elif action == "remove":
                if rbt.search(rbt.root, nod) == sent:
                   print("TreeError")
                    
                else:
                    nod = rbt.search(rbt.root, nod)
                    rbt.remove(nod)

            elif action == "search":
                if rbt.search(rbt.root, nod) != sent:
                    print("Found")
                
                else:
                    print("NotFound")

            elif action == "inprint":
                root = rbt.root
                if root == sent:
                    print("Empty") 
                else:
                    l = rbt.to_list_inorder(root)
                    print(' '.join(l)) #formatted to print the correct way as specified
                
            
            del lis[:] #I used .clear() but after testing on ix-dev, the clear method did not work so I found this online at Stack Overflow: https://stackoverflow.com/questions/850795/different-ways-of-clearing-lists




if __name__ == "__main__":
    driver()
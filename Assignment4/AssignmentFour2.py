import sys

#my inorder list to evaluate the correct expression
lis_in = []
#my postorder list to evaluate the correct value of the expression
lis_pos = []


class STNode:

    def __init__(self, x: str):
        self.key = x
        self.left = None
        self.right = None


class SyntaxTree:
    #Starter ccode given, modified to fix indexing issue.
    def init_helper(self, i: int, l: 'list of strings') -> STNode:
        if i >= len(l):
            return None
        node = STNode(l[i])
        node.left = self.init_helper(2 * i + 1, l)
        node.right = self.init_helper(2 * i + 2, l)
        return node

    def __init__(self, l: 'list of strings') -> 'complete syntax tree':
        self.root = self.init_helper(0, l)

    def to_list_inorder(self, x):
        if x != None:
            if x.left != None: #we append a left-bracket when we know there is going to be another number value (the left child is not blank)
                lis_in.append('(')
            self.to_list_inorder(x.left)
            lis_in.append(str(x.key)) #after checking the left, we append the value at the left.
            self.to_list_inorder(x.right)
            if x.right != None:
                lis_in.append(')') #after appending the value, we can put in the right bracket.
        exp = ''.join(lis_in) #join list together to achieve the correct formatting output
        return exp


    def to_list_postorder(self, x):
        if x.left == None and x.right == None: #once we get to a leaf node, we return the key value, as an integer (this is our base case).
            return int(x.key)
        else:
            left = self.to_list_postorder(x.left) #basically, the ideas is this: obtain our number values, then perform whatever operation on them.
            right = self.to_list_postorder(x.right)
            if (x.key == "+"):  #Checking for the three possible operand options.
                return (left + right)
            elif (x.key == '-'):
                return (left - right)
            elif (x.key == '*'):
                return (left * right)






def driver():
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        in_data = f.readline().strip().split()    
        st = SyntaxTree(in_data)
        inorder = st.to_list_inorder(st.root)
        print(inorder)
        post = st.to_list_postorder(st.root)
        print(post)


if __name__ == "__main__":
    driver()

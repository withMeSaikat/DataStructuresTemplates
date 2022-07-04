class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, val): # Working
        if self.root == None:
            self.root = Node(val)
        else:
            self.insertUtil(val, self.root)
            
    def insertUtil(self, val, curr):
        if curr.val > val:
            if curr.left == None:
                curr.left = Node(val)
            else:
                self.insertUtil(val, curr.left)
        else:
            if curr.right == None:
                curr.right = Node(val)
            else:
                self.insertUtil(val, curr.right)
    
    def inOrder(self): # Working
        self.inOrderUtil(self.root)
        print()

    def inOrderUtil(self, curr):
        if curr == None:
            return
        
        self.inOrderUtil(curr.left)
        print(curr.val, end=" ")
        self.inOrderUtil(curr.right)
    
    def search(self, val, curr=None):
        if curr == None:
            curr = self.root
        return self.searchUtil(val, curr)
    
    def searchUtil(self, val, curr):
        if curr == None:
            return None
        
        if curr.val == val:
            return curr
        
        elif curr.val > val:
            return self.searchUtil(val, curr.left)
        else:
            return self.searchUtil(val, curr.right)
    
    def getMax(self, curr=None): # Working
        if curr == None:
            curr = self.root
        
        while curr.right != None:
            curr = curr.right
        
        return curr
    
    def getMin(self, curr=None): # Working
        if curr == None:
            curr = self.root
        
        while curr.left != None:
            curr = curr.left
        
        return curr
    
    def delete(self, val, curr): # Working
        if curr == None:
            return curr
        
        if curr.val > val:
            curr.left = self.delete(val, curr.left)
        elif curr.val < val:
            curr.right = self.delete(val, curr.right)
        else:
            if curr.left == None:
                return curr.right
            if curr.right == None:
                return curr.left
            
            replace = self.getMin(curr.right)
            curr.val = replace.val
            curr.right = self.delete(replace.val, curr.right)
        return curr

    def rightAncestor(self, val):
        return self.rightAncestorUtil(val, curr, mx)
    
    def rightAncestorUtil(self, val, curr, mx=float('inf')):
        if curr == None or curr == self.root:
            return None
        if curr.val == val:
            return mx
        elif curr.val > val:
            return self.rightAncestorUtil(val, curr.left, curr.val)
        else:
            return self.rightAncestorUtil(val, curr.right, mx)

    def isBSTUsingTopDown(self, root, mn=float('-inf'), mx=float('inf')):
        if root is None:
            return True
        
        if root.val > mx or root.val < mn:
            return False
        
        isLeftValid = self.isBSTUsingTopDown(root.left, mn, root.val)
        isRightValid = self.isBSTUsingTopDown(root.right, root.val, mx)

        if isLeftValid and rightValid:
            return True
        
        return False

    def isBSTUsingBottomUp(self, root):
        if root is None:
            return [True, float('inf'), float('-inf')]
        
        left = self.isBSTUsingBottomUp(root.left)
        right = self.isBSTUsingBottomUp(root.right)

        res = True

        if root.val < left[1] or root.val > right[2]:
            res = False

        if left[0] == False or right[0] == False:
            res = False
        
        return [res, min(root.val, left[1]), max(root.val, right[2])]
        
def main():
    bst = BST()
    while True:
        num = input()
        if num == "q":
            bst.inOrder()
            break
        bst.insert(int(num))
        bst.inOrder()

    mn = bst.getMin()
    if mn == None:
        mn = Node(-1)
    
    mx = bst.getMax()
    if mx == None:
        mx = Node(-1)
    
    print('Min: ', mn.val)
    print('Max: ', mx.val)
    bst.delete(8, bst.root)
    bst.inOrder()
    bst.delete(-1, bst.root)
    bst.inOrder()
if __name__ == "__main__":
    main()
        
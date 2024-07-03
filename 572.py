from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        else:
            l = self.isEqual(root.left, subRoot.left)
            if not l:
                return False
            r = self.isEqual(root.right, subRoot.right)
            if not r:
                return False

            return True

    def treeTraversal(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if not root:
            return
        elif root.val == subRoot.val:
            res = self.isEqual(root, subRoot)
            if res:
                return res

        l = self.treeTraversal(root.left, subRoot)
        if l:
            return l

        r = self.treeTraversal(root.right, subRoot)
        if r:
            return r

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.treeTraversal(root, subRoot)


if __name__ == '__main__':
    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n3 = TreeNode(4)
    n4 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(4)
    n7 = TreeNode(1)
    n8 = TreeNode(2)
    # n9 = TreeNode(0)  "uncomment to check second case"

    # subTree
    n6.left = n7
    n6.right = n8

    # mainTree
    n4.left = n3
    n4.right = n5
    n3.left = n2
    n3.right = n1
    # n8.left = n9

    main = Solution()
    main.isSubtree(n4, n6)

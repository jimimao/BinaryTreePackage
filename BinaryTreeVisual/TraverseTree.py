"""
done:
    层次遍历
    hierarchical_traverse

    先序，中序，后序遍历
    preorder_Recursion
    inorder_Recursion
    postorder_Recursion
to-do:
    preorder_iteration
    inorder_iteration
    postorder_iteration
"""
def max_depth(root):
    """
    求树最大深度
    :param root:
    :return:
    """
    nodelist = [(1, root)]
    while nodelist:
        depth, node = nodelist.pop(0)
        if node.left:
            nodelist.append((depth + 1, node.left))
        if node.right:
            nodelist.append((depth + 1, node.right))
    return depth


def hierarchical_traverse(root):
    """
    hieorder 层次遍历二叉树
    :param root: 树根
    :return hieorder, 层次遍历二叉树
    """
    if not root:
        return [[]]
    # 求最大深度
    depth = max_depth(root)
    m, n = 2*depth-1,2**depth-1
    hieorder = [[' ' for _ in range(n)] for _ in range(m)]
    # 画输出矩阵
    nodelist = [(0,n//2,root)]
    while nodelist:
        row, col, node = nodelist.pop(0)
        hieorder[row][col] = str(node.val)
        if node.left:
            hieorder[row + 1][col - (depth - (row + 2) // 2) + 1] = '/'
            nodelist.append((row+2,col - (depth - (row+3) // 2),node.left))
        if node.right:
            hieorder[row + 1][col + (depth - (row + 2) // 2) - 1] = '\\'
            nodelist.append((row+2,col + (depth - (row+3) // 2),node.right))
    return hieorder


def preorder_Recursion(root):
    """
    preorder 递归先序遍历二叉树
    :param root: 树根
    :return preorder, 先序遍历的list
    """
    if not root:
        return []
    preorder = []
    def rec(root):
        preorder.append(root.val)
        if root.left:
            rec(root.left)
        if root.right:
            rec(root.right)
    rec(root)
    return preorder
def inorder_Recursion(root):
    """
    inorder 递归中序遍历二叉树
    :param root: 树根
    :return inorder, 中序遍历的list
    """
    if not root:
        return []
    inorder = []
    def rec(root):
        if root.left:
            rec(root.left)
        inorder.append(root.val)
        if root.right:
            rec(root.right)
    rec(root)
    return inorder
def postorder_Recursion(root):
    """
    postorder 递归后序遍历二叉树
    :param root: 树根
    :return preorder, 后序遍历的list
    """
    if not root:
        return []
    postorder = []

    def rec(root):
        if root.left:
            rec(root.left)
        if root.right:
            rec(root.right)
        postorder.append(root.val)

    rec(root)
    return postorder
# def preorder_iteration(root):
#     """
#     preorder 迭代先序遍历二叉树
#     :param root: 树根
#     :return preorder, 先序遍历的list
#     """
# def inorder_iteration(root):
#     """
#     inorder 迭代中序遍历二叉树
#     :param root: 树根
#     :return inorder, 中序遍历的list
#     """
# def postorder_iteration(root):
#     """
#     postorder 迭代后序遍历二叉树
#     :param root: 树根
#     :return postrder, 后序遍历的list
#     """
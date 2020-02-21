""" Visualition of Binary Tree
:param root : the root of an Binary Tree
:return
    //              1
    //           /     \
    //          2       3
    //         /       / \
    //        4       5   6
    //         \         /
    //          7       8
"""
from .TraverseTree import hierarchical_traverse

def BinaryTreeVisual(root):
    visualBTree = hierarchical_traverse(root)
    for item in visualBTree:
        print("".join(item))
    # print(visualBTree)
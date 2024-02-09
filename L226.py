#!/usr/bin/env python3

### Import Statements ###

from test import test

from binarytree import *

### Functions ###


def invert_tree(root: TreeNode) -> TreeNode:
    """L226 (Easy)

    Args:
        root (TreeNode): The root of the binary tree

    Returns:
        TreeNode: An inverted tree where every node's left and right are switched
    """
    if root:
        invert_tree(root.left)
        invert_tree(root.right)
        root.left, root.right = root.right, root.left
    return root


if __name__ == "__main__":
    tree = make_tree([4, 2, 7, 1, 3, 6, 9])
    print_tree(tree)
    inverted_tree = invert_tree(tree)
    print_tree(tree)

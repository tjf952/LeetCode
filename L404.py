#!/usr/bin/env python3

### Import Statements ###

from test import test

from binarytree import *

### Functions ###


def sumOfLeftLeaves(root: TreeNode) -> int:
    """L404 (Easy)

    Args:
        root (TreeNode): The root of a binary tree

    Returns:
        int: The sum of left leaves
    """
    if not root:
        return 0
    elif root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


if __name__ == "__main__":
    tree_list = [3, 9, 20, None, None, 15, 7]
    root = make_tree(tree_list)
    test(sumOfLeftLeaves(root), 24)

#!/usr/bin/env python3

### Import Statements ###

from test import test

### Classes ###


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### Functions ###


def make_tree(a: list) -> TreeNode:
    """Makes tree from list

    Args:
        a (list): Given integer list

    Returns:
        TreeNode: Root of binary tree
    """
    root = TreeNode(a[0])
    queue = [root]
    i = 1

    while queue and i < len(a):
        current = queue.pop(0)
        current.left = TreeNode(a[i])
        queue.append(current.left)
        i += 1

        if i < len(a):
            current.right = TreeNode(a[i])
            queue.append(current.right)
            i += 1

    return root


def print_tree(root: TreeNode) -> None:
    """Prints tree using inorder traversal

    Args:
        root (TreeNode): The root of the binary tree
    """
    if root:
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)


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
    print()
    inverted_tree = invert_tree(tree)
    print_tree(tree)
    print()

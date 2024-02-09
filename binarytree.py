#!/usr/bin/env python3


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
        list_val = a[i]
        if list_val is not None:
            current.left = TreeNode(list_val)
            queue.append(current.left)
        i += 1
        if i < len(a):
            list_val = a[i]
            if list_val is not None:
                current.right = TreeNode(list_val)
                queue.append(current.right)
            i += 1

    return root


def print_tree(root: TreeNode) -> None:
    """Prints tree using inorder traversal

    Args:
        root (TreeNode): The root of the binary tree
    """

    def helper(root: TreeNode) -> None:
        if root:
            helper(root.left)
            print(root.val, end=" ")
            helper(root.right)

    helper(root)
    print()

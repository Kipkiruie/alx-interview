#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Function to determine if all the boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key < n:
                    stack.append(key)
    return len(opened) == n
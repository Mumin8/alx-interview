#!/usr/bin/python3
# 0-lockboxes.py that is the module 

def canUnlockAll(boxes):
    '''
    This function checks if all the boxes can be unlocked.

    Returns:
        True if all the boxes can be unlocked.
        False if all the boxes cannot be unlocked.
    '''
    n = len(boxes)
    keys = set([0])
    opened = set()

    while keys:
        key = keys.pop()
        opened.add(key)
        keys.update(set(boxes[key]) - opened)

    return len(opened) == n

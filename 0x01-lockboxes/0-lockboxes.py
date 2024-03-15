#!/usr/bin/python3
'''a function that will check if all boxes can be opened''' 

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

#!/usr/bin/python3
# 0x01-lockboxes


def canUnlockAll(boxes):
    '''
    this checks if all the boxes can be unlocked

    return:
        True if all the boxes can be unlocked
        False if all the boxes cannot be unlocked
    '''
    n = len(boxes)
    keys = set([0])
    opened = set()
    
    while keys:
        key = keys.pop()
        opened.add(key)
        keys.update(set(boxes[key]) - opened)

    return len(opened) == n

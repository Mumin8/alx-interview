def canUnlockAll(boxes):
    n = len(boxes)
    keys = set([0])
    opened = set()

    while keys:
        key = keys.pop()
        opened.add(key)
        keys.update(set(boxes[key]) - opened)

    return len(opened) == n

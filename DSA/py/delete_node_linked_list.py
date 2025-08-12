
def deleteNode(node):
    while node.next:
        node.val = node.next.val
        if not node.next.next:
            node.next = None
        else:
            node = node.next
# https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    """
    linked list has a next property that indicates what node it connects to
    please note the constraint here is that the linked lists should be 1 <= n <= 100
    cycles will cause the list to repeat forever if we don't break at some point
    if more than 100 nodes are observed, we've hit a cycle and there is a loop
    """
    current_node = head
    i = 0
    while i < 100:
        current_node = current_node.next
        i += 1
        if not current_node:
            return False  # If we run this and hit a none we've terminated the LL and there is no cycle
    return True

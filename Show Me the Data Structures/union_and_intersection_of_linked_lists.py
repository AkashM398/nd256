from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next


def union(llist_1, llist_2):
    # Your Solution Here
    union = set()
    union_llist = LinkedList()
    for un_1 in llist_1:
        union.add(un_1)
    for un_2 in llist_2:
        union.add(un_2)
    for un in union:
        union_llist.append(un)

    return union_llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection = set()
    intersection_llist = LinkedList()
    for i in llist_1:
        if i in llist_2:
            intersection.add(i)

    for v in intersection:
        intersection_llist.append(v)

    return intersection_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(linked_list_1)
print(linked_list_2)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(linked_list_3)
print(linked_list_4)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))


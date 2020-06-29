
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def list_print(self):
        t = self.head
        while t is not None:
            if (t.next is None):
                print(t.value)
                t = t.next
                continue

            print(t.value, end = " -> "),
            t = t.next


def list_addition(l1, l2):
    a = l1.head
    b = l2.head
    l3 = LinkedList()
    up = 0

    t = Node((a.value + b.value + up) % 10)
    up = (a.value + b.value + up) // 10
    l3.head = t

    a = a.next
    b = b.next

    while a is not None and b is not None: 
        t.next = Node((a.value + b.value + up) % 10)
        up = (a.value + b.value + up) // 10

        a = a.next
        b = b.next
        t = t.next

    while a is not None:
        t.next = Node((a.value + up) % 10)
        up = (a.value + up) // 10

        a = a.next
        t = t.next

    while b is not None:
        t.next = Node((b.value + up) % 10)
        up = (b.value + up) // 10

        b = b.next
        t = t.next

    return l3


def int_to_list(i):
    l = LinkedList()
    
    t = Node(i % 10)
    i //= 10
    l.head = t

    while i > 0:
        t.next = Node(i % 10)
        i //= 10
        t = t.next

    return l


# Main
p = 84
q = 864

l1 = int_to_list(p)
l2 = int_to_list(q)

list_addition(l1, l2).list_print()
print(p + q)

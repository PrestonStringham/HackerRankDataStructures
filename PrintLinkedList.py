# URL: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    current = head
    print(current.data)
    while current.next is not None:
        print(current.next.data)
        current = current.next

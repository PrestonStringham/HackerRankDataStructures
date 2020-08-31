# URL: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

#This problem is broken on HackerRank... 


def insertNodeAtTail(head, data):
    
    sys.setrecursionlimit(1000000) 
    if head == None:

        return SinglyLinkedListNode(data)
    else:
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
        else:
            insertNodeAtTail(head.next,data)
    return  llist.head

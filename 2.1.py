from typing import Any

class Node:

    value: Any
    next: 'Node'


class LinkedList:

    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def len(self) -> Node:
        temp = self.head
        wyn = 0
        while(True):
            wyn=wyn+1
            if (temp.next == None):
                break
            temp = temp.next
        return wyn;

    def push(self, value: Any) -> None:

        temp = Node()
        f = False
        if(self.head == None):
            f = True
        temp.value = value
        temp.next = self.head
        self.head = temp
        if (f == True):
            self.tail = self.head
            f = False

    def append(self, value: Any) -> None:

        temp = Node()
        temp.value = value
        temp.next = None
        if(self.tail != None):
            self.tail.next = temp
        self.tail = temp
        if(self.head == None):
            self.head = self.tail

    def show(self) -> Node:
        temp = self.head
        while(True):
            print(temp.value)
            if (temp.next == None):
                break
            temp = temp.next

    def node(self, at: int) -> Node:

        temp = self.head
        for i in range(1, at):
            temp = temp.next
        return temp

    def insert(self, value: Any, after: Node) -> None:

        temp = Node()
        temp.value = value
        temp.next = after.next
        after.next = temp

    def pop(self) -> Any:

        temp = self.head
        self.head = self.head.next
        return temp

    def remove_last(self) -> Any:

        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        t = temp.next
        temp.next = None
        self.tail = temp
        return  t

    def remove(self, after: Node) -> Any:

        temp = after.next.next
        after.next = after.next.next
        return temp

    def print(self):

        print(str(self.head.value) + " -> " + str(self.head.next.value))

list_ = LinkedList()
list_.append(0)
list_.append(1)
list_.print()

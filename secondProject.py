from typing import Any, Callable
import sys as system

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'
    parent: 'BinaryNode'

    def __init__(self, v):
        self.value = v
        self.left_child = None
        self.right_child = None
        self.parent = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self):
        return self.left_child or self.right_child

    def add_left_child(self, value: Any):
        lc = BinaryNode(value)
        lc.parent = self
        self.left_child = lc

    def add_right_child(self, value: Any):
        rc = BinaryNode(value)
        rc.parent = self
        self.right_child = rc

    def goToLeft(self):
        if self.left_child:
            return self.left_child.goToLeft()
        if not self.left_child and self.right_child:
            return self.right_child.goToLeft()
        return self


    def traverse_post_order(self, visit: Callable[[Any], None]):

        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None], was = []):

        visit(self)
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)

    def traverse_in_order(self, visit: Callable[[Any], None], was = []):

        if self.left_child:
            self.left_child.traverse_post_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_post_order(visit)

class BinaryTree:
    root: BinaryNode

    def __init__(self, r: BinaryNode):
        self.root = r

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self, node: 'BinaryNode', l: int):

        if node.parent is None:
            for i in range(l):
                system.stdout.write("  ")
            print(" " + str(node.value) + "  ")
        if node.left_child:
            for i in range(l):
                system.stdout.write("  ")
            system.stdout.write(str(node.left_child.value))
        if node.right_child and node.right_child.is_leaf() is None:
            system.stdout.write("  " + str(node.right_child.value))
        elif node.right_child:
            print("  " + str(node.right_child.value))
        if node.left_child:
            self.show(node.left_child, l-1)
        if node.right_child:
            self.show(node.right_child, l-1)

def closest_parent(tree: 'BinaryTree', first_node: BinaryNode, second_node: BinaryNode):

    tab = []
    def goThruFN(node: 'BinaryNode'):
        tab.append(node)
        if node.parent:
            goThruFN(node.parent)
    goThruFN(first_node)
    temp = []
    def goThruSN(node: 'BinaryNode'):
        for i in tab:
            if node == i:
                temp.append(node)
        if node.parent:
            goThruSN(node.parent)
    goThruSN(second_node)
    return temp[0]s

bn = BinaryNode(10)
bn.add_left_child(9)
bn.add_right_child(2)
bn.left_child.add_left_child(1)
bn.left_child.add_right_child(3)
bn.right_child.add_left_child(4)
bn.right_child.add_right_child(6)

bn2 = BinaryTree(bn)
print(closest_parent(bn2, bn.left_child.left_child, bn.left_child.right_child).value)

class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.prev = None
        self.value = value


class DoubleLinkedlist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0


    def add(self, value):
        node = Node(value)

        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        self.size += 1


    def remove(self, value):
        node = self.head

        while node is not None:
            if node.value is value:
                self.__remove_node(node)
                
            node = node.next


    def remove_last_node(self):
        if self.tail is not None:
            self.__remove_node(self.tail)


    def remove_first_node(self):
        if self.head is not None:
            self.__remove_node(self.head)


    def __remove_node(self, node: Node):
            if node.prev is None:
                self.head = node.next
            else:
                node.prev.next = node.next

            if node.next is None:
                self.tail = node.prev
            else:
                node.next.prev = node.prev

            self.size -= 1


    # this will format the instance of this class when printed
    def __str__(self) -> str:
        values = []
        node = self.head
        while node is not None:
            values.append(node.value)
            node = node.next
        return f'[{", ".join(str(value) for value in values)}]'


myList = DoubleLinkedlist()

myList.add(1)
myList.add(2)
myList.add(3)

print(f'size of the list: {myList.size}')
print(myList)

myList.remove_first_node()
print(f'size of the list: {myList.size}')
print(myList)

myList.remove_last_node()
print(f'size of the list: {myList.size}')
print(myList)

myList.remove(2)
print(f'size of the list: {myList.size}')
print(myList)

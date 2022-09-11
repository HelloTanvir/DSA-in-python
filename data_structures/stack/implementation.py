class Stack:
    def __init__(self) -> None:
        self.__list = []

    def push(self, val):
        self.__list.append(val)

    def pop(self):
        if self.is_empty():
            return None

        return self.__list.pop()

    def is_empty(self):
        return len(self.__list) == 0

    def peek(self):
        return self.__list[-1]

    def __len__(self):
        return len(self.__list)

class Queue:
    def __init__(self) -> None:
        self.__list = []

    def enqueue(self, val):
        self.__list.append(val)

    def dequeue(self):
        if self.is_empty():
            return None

        self.__list = self.__list[1:]
        return self.__list

    def is_empty(self):
        return len(self.__list) == 0

    def front(self):
        if self.is_empty():
            return None

        return self.__list[0]

    def __len__(self):
        return len(self.__list)

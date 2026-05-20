class Pila:
    def __init__(self):
        self._items = []

    def push(self, elemento):
        self._items.append(elemento)

    def pop(self):
        if self.empty():
            return None
        return self._items.pop()

    def top(self):
        if self.empty():
            return None
        return self._items[-1]

    def empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def print_stack(self):
        for i in range(len(self._items) - 1, -1, -1):
            print(self._items[i], end=" ")
        print()
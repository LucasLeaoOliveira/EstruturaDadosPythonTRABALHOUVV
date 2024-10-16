class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []  # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack."""
        if self.is_empty():
            print('Pilha vazia')
            return None
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)."""
        if self.is_empty():
            print('Pilha vazia')
            return None
        return self._data.pop()  # remove the last item

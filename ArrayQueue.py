class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 30  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._first = 0
        self._last = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            print('Fila vazia')
            return None
        return self._data[self._first]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            print('Fila vazia')
            return None
        answer = self._data[self._first]
        self._data[self._first] = None  # help garbage collection
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._first + self._size) % len(self._data)
        self._data[avail] = e  # add e as the new last element
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[(self._first + k) % len(old)]  # shift indices
        self._first = 0  # front has been realigned

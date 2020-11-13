"""
Simple hash table implementation
"""


class HashTableIter():
    """
    Hash table itetrator
    """
    def __init__(self, hashTable):
        self._index = -1
        self._data = hashTable.get_data()
        self._max = len(self._data)

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index < self._max:
            return self._data[self._index]
        raise StopIteration


class HashTable():
    """
    Simple hash table
    """
    def __init__(self, lenght=100):
        self._data = [[] for _ in range(lenght)]
        self._len = lenght
        self._elems = 0

    def add(self, elem):
        """
        Add item in hash table
        """
        if elem not in self._data[hash(elem) % self._len]:
            self._data[hash(elem) % self._len].append(elem)
            self._elems += 1

    def remove(self, elem):
        """
        Remove item from hash table
        """
        for i in range(len(self._data[hash(elem) % self._len])):
            if self._data[hash(elem) % self._len][i] == elem:
                self._data[hash(elem) % self._len].pop(i)
                self._elems -= 1
                break

    def get_data(self):
        """
        Get containing data
        """
        return [i for s in self._data for i in s]

    def __contains__(self, item):
        for i in range(len(self._data[hash(item) % self._len])):
            if self._data[hash(item) % self._len][i] == item:
                return True
        return False

    def __len__(self):
        return self._elems

    def __iter__(self):
        return HashTableIter(self)

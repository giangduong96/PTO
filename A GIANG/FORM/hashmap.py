import random
class HashMapBase:
    def __init__(self, cap = 11, p = 109345121):
        """Create an empty hash-table map"""
        self._table = cap*[None]
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p -1)
        self._shift = random.randrange(p)

    def _has_function(self, k):
        return (hash(k) *self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._has_function(k)

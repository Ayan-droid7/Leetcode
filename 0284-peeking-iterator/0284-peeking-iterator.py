class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked_val = None
        if self.iterator.hasNext():
            self.peeked_val = self.iterator.next()

    def peek(self):
        return self.peeked_val

    def next(self):
        val = self.peeked_val
        if self.iterator.hasNext():
            self.peeked_val = self.iterator.next()
        else:
            self.peeked_val = None
        return val

    def hasNext(self):
        return self.peeked_val is not None
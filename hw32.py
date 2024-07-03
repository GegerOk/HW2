class EvenNumbers:
    def __init__(self, start, end):
        self.i = start
        self.end = end
    def __iter__ (self):
        return self
    def __next__ (self):
        self.i += 1
        if self.i == self.end:
            raise StopIteration
        elif self.i % 2 == 0:
            return self.i
        else:
            return ""
        
Ev = EvenNumbers(10, 25)
for i in Ev:
    print(i)
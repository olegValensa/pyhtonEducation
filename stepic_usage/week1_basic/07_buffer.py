class Buffer:
    elements = []

    def __init__(self):
        pass

    def add(self, *a):
        for element in a:
            self.elements.append(element)
            if len(self.elements) == 5:
                print(sum(self.elements))
                del self.elements[:]

    def get_current_part(self):
        return self.elements

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()
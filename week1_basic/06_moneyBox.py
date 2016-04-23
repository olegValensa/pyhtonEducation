class MoneyBox:
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        return v <= self.capacity - self.count

    def add(self, v):
        if self.can_add(v):
            self.count += v


from datetime import datetime
print(datetime.utcnow().isoformat(' '))

a = MoneyBox(20)
print(a.capacity)
print(a.count)
a.add(5)
print(a.capacity)
print(a.count)
a.add(17)
print(a.capacity)
print(a.count)

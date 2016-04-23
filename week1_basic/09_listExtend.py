class ExtendedStack(list):
    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1+top2)

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1-top2)

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1*top2)

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1//top2)

x = ExtendedStack([1, 2, 3])
print(x)
x.sum()
print(x)
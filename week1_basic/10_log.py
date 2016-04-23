import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, p_object):
        super(LoggableList, self).append(p_object)
        self.log(p_object)

x = Loggable()
x.log('kms')

y = LoggableList([1, 2, 3])
y.log('2')
y.append(6)
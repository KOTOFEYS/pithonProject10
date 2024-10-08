
from turtledemo.penrose import start

class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.stop > 0:
            if self.stop < self.pointer:
                raise StopIteration()
        elif self.step > 0 and self.stop:
            if self.stop < self.pointer:
                raise StopIteration()
        elif self.step < 0 and self.stop > 0:
            if self.stop > self.pointer:
                raise StopIteration()
        else:
            raise StopIteration
        return self.pointer

    def __iter__(self):
        self.start = self.start
        self.pointer = self.start - self.step
        self.stop = self.stop
        return self

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError:
        print('Шаг указан неверно')
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

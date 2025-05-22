from threading import Event

class Foo:
    def __init__(self):
        pass
        self.firstDone = Event()
        self.secondDone = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstDone.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.firstDone.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.secondDone.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.secondDone.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
from functools import wraps

class myclass:
    def __init__(self):
        self.start = False

    def _with_check(f):
        print('ok')
        @wraps(f)
        def wrapped(inst):
            if inst.check():
                return
            return inst
        return wrapped

    def check(self):
        return self.start

    @_with_check
    def doA(self):
        print('A')

    @_with_check
    def doB(self):
        print('B')

myclass().doB()

class Test:
    def __init__(self, func):
        self.func = func
        # self.is_run = is_run
        
    def __call__(self):
        # if self.is_run:
        print(self.func)
        self.func()

def test(func):
    func()
class Test:

    def __init__(self, param):
        self.param = param


a = Test(1)
b = a
b.param = 2

print(a.param)

# Have a nice day ♥ 
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def division(self):
        try:
            avara = self.a / self.b
        except ZeroDivisionError:
            avara = "nakupuninin"
        return avara
    #AAAAAA
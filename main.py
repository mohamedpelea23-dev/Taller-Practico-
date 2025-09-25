class operaciones:
    def __init__(self,a,b):
        self._a=a
        self._b=b 
    def suma(self):
        return self._a + self._b
    def resta(self):
        return self._a - self._b
if __name__ == "__main__":
    op = operaciones(5, 3)
    print("Suma:", op.suma())
    print("Resta:", op.resta())
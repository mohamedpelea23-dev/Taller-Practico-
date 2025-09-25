class operaciones:
    def __init__(self,a,b):
        self._a=a
        self._b=b 
    def suma(self):
        return self._a + self._b
    def resta(self):
        return self._a - self._b
    def division(self):
        if self._b == 0:
            return "error: division por cero"
        return self._a / self._b
    def multiplicar(self):
        return self._a * self._b
if __name__ == "__main__":
    op = operaciones(5, 3)
    print("Suma:", op.suma())
    print("Resta:", op.resta())
    print("Multiplicación:", op.multiplicar())
    print("División:", op.division())





class PDV:

    def __init__(self, saldo, num):
        self._saldo = saldo
        self._num = num

    def getSaldo(self):
        return self._saldo
    
    def setSaldo(self, x):
        self._saldo = x
    
    def getNum(self):
        return self._num
    
    def setNum(self, x):
        self._num = x


p1 = PDV(1000, 2)

print(p1.getSaldo())
p1.setSaldo(500)
print(p1.getSaldo())

print(p1.getNum())
p1.setNum(1)
print(p1.getNum())




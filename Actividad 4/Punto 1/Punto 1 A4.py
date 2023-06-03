class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self._saldo = saldo  
        self._num_consignaciones = 0  
        self._num_retiros = 0  
        self._tasa_anual = tasa_anual  
        self._comision_mensual = 0.0  

    def consignar(self, cantidad):
        self._saldo += cantidad
        self._num_consignaciones += 1

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("Error: Fondos insuficientes.")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 100) / 12
        self._saldo += self._saldo * interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        print("Saldo: ", self._saldo)
        print("Comisión Mensual: ", self._comision_mensual)
        print("Número de transacciones: ", self._num_consignaciones + self._num_retiros)


class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._cuenta_activa = saldo >= 10000  

    def consignar(self, cantidad):
        if self._cuenta_activa:
            super().consignar(cantidad)
        else:
            print("Error: Cuenta inactiva.")

    def retirar(self, cantidad):
        if self._cuenta_activa:
            super().retirar(cantidad)
        else:
            print("Error: Cuenta inactiva.")

    def extracto_mensual(self):
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print("Cuenta activa: ", self._cuenta_activa)


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0  

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            super().retirar(cantidad)
        else:
            self._sobregiro += cantidad - self._saldo
            self._saldo = 0

    def consignar(self, cantidad):
        if self._sobregiro > 0:
            if cantidad <= self._sobregiro:
                self._sobregiro -= cantidad
            else:
                self._saldo += cantidad - self._sobregiro
                self._sobregiro = 0
        else:
            super().consignar(cantidad)

    def imprimir(self):
        super().imprimir()
        print("Sobregiro: ", self._sobregiro)


def main():
    cuenta_ahorros = CuentaAhorros(15000, 2.5)
    
    cuenta_ahorros.consignar(5000)
    
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    
    cuenta_ahorros.extracto_mensual()
    
    cuenta_ahorros.imprimir()


main()

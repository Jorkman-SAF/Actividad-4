class Cuenta:
    def __init__(self, saldo, tasa_anual):
        # Constructor que inicializa los atributos de la cuenta
        self._saldo = saldo  # Atributo de acceso protegido (_saldo)
        self._num_consignaciones = 0  # Atributo de acceso protegido (_num_consignaciones)
        self._num_retiros = 0  # Atributo de acceso protegido (_num_retiros)
        self._tasa_anual = tasa_anual  # Atributo de acceso protegido (_tasa_anual)
        self._comision_mensual = 0.0  # Atributo de acceso protegido (_comision_mensual)

    def consignar(self, cantidad):
        # Método para consignar una cantidad de dinero en la cuenta
        self._saldo += cantidad
        self._num_consignaciones += 1

    def retirar(self, cantidad):
        # Método para retirar una cantidad de dinero de la cuenta
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("Error: Fondos insuficientes.")

    def calcular_interes_mensual(self):
        # Método para calcular el interés mensual de la cuenta
        interes_mensual = (self._tasa_anual / 100) / 12
        self._saldo += self._saldo * interes_mensual

    def extracto_mensual(self):
        # Método para generar el extracto mensual de la cuenta
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()

    def imprimir(self):
        # Método para imprimir los valores de los atributos de la cuenta
        print("Saldo: ", self._saldo)
        print("Comisión Mensual: ", self._comision_mensual)
        print("Número de transacciones: ", self._num_consignaciones + self._num_retiros)


class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        # Constructor de la clase CuentaAhorros
        super().__init__(saldo, tasa_anual)
        self._cuenta_activa = saldo >= 10000  # Atributo de acceso protegido (_cuenta_activa)

    def consignar(self, cantidad):
        # Método para consignar dinero en la cuenta de ahorros
        if self._cuenta_activa:
            super().consignar(cantidad)
        else:
            print("Error: Cuenta inactiva.")

    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta de ahorros
        if self._cuenta_activa:
            super().retirar(cantidad)
        else:
            print("Error: Cuenta inactiva.")

    def extracto_mensual(self):
        # Método para generar el extracto mensual de la cuenta de ahorros
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()

    def imprimir(self):
        # Método para imprimir los valores de los atributos de la cuenta de ahorros
        super().imprimir()
        print("Cuenta activa: ", self._cuenta_activa)


class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        # Constructor de la clase CuentaCorriente
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0  # Atributo de acceso protegido (_sobregiro)

    def retirar(self, cantidad):
        # Método para retirar dinero de la cuenta corriente
        if cantidad <= self._saldo:
            super().retirar(cantidad)
        else:
            self._sobregiro += cantidad - self._saldo
            self._saldo = 0

    def consignar(self, cantidad):
        # Método para consignar dinero en la cuenta corriente
        if self._sobregiro > 0:
            if cantidad <= self._sobregiro:
                self._sobregiro -= cantidad
            else:
                self._saldo += cantidad - self._sobregiro
                self._sobregiro = 0
        else:
            super().consignar(cantidad)

    def imprimir(self):
        # Método para imprimir los valores de los atributos de la cuenta corriente
        super().imprimir()
        print("Sobregiro: ", self._sobregiro)


def main():
    # Crear una instancia de CuentaAhorros con saldo inicial de 15000 y tasa anual del 2.5%
    cuenta_ahorros = CuentaAhorros(15000, 2.5)
    
    # Consignar 5000 en la cuenta de ahorros
    cuenta_ahorros.consignar(5000)
    
    # Retirar 10000 de la cuenta de ahorros
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    cuenta_ahorros.retirar(2000)
    
    # Generar el extracto mensual de la cuenta de ahorros (calcular intereses y aplicar comisiones)
    cuenta_ahorros.extracto_mensual()
    
    # Imprimir los valores de los atributos de la cuenta de ahorros
    cuenta_ahorros.imprimir()


main()

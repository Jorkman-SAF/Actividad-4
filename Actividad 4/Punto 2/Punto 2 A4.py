class Inmueble:
    def __init__(self, identificador, area, direccion):
        self._identificador = identificador
        self._area = area
        self._direccion = direccion
        self._valor_compra = self.calcular_valor_compra()

    def calcular_valor_compra(self):
        raise NotImplementedError("Método abstracto sin implementar")

    def imprimir(self):
        print(f"Inmueble ID: {self._identificador}")
        print(f"Área: {self._area} metros cuadrados")
        print(f"Dirección: {self._direccion}")
        print(f"Valor de compra: ${self._valor_compra}")


class InmuebleVivienda(Inmueble):
    def __init__(self, identificador, area, direccion, num_habitaciones, num_banos):
        super().__init__(identificador, area, direccion)
        self._num_habitaciones = num_habitaciones
        self._num_banos = num_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones: {self._num_habitaciones}")
        print(f"Número de baños: {self._num_banos}")


class CasaRural(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, num_habitaciones, num_banos, distancia_cabecera, altitud):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 1500000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera: {self._distancia_cabecera} km")
        print(f"Altitud: {self._altitud} metros")


class CasaConjuntoCerrado(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, num_habitaciones, num_banos, valor_administracion, areas_comunes):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)
        self._valor_administracion = valor_administracion
        self._areas_comunes = areas_comunes

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 2500000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()
        print(f"Valor de administración: ${self._valor_administracion}")
        print(f"Áreas comunes: {self._areas_comunes}")


class CasaIndependiente(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, num_habitaciones, num_banos, num_pisos):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)
        self._num_pisos = num_pisos

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 3000000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self._num_pisos}")


class ApartaEstudio(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, num_banos):
        super().__init__(identificador, area, direccion, 1, num_banos)

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 1500000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()


class ApartamentoFamiliar(InmuebleVivienda):
    def __init__(self, identificador, area, direccion, num_habitaciones, num_banos):
        super().__init__(identificador, area, direccion, num_habitaciones, num_banos)

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 2000000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()


class LocalComercial(Inmueble):
    def __init__(self, identificador, area, direccion, localizacion, centro_comercial):
        super().__init__(identificador, area, direccion)
        self._localizacion = localizacion
        self._centro_comercial = centro_comercial

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 3000000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()
        print(f"Localización: {self._localizacion}")
        print(f"Centro comercial: {self._centro_comercial}")


class Oficina(Inmueble):
    def __init__(self, identificador, area, direccion, es_gobierno):
        super().__init__(identificador, area, direccion)
        self._es_gobierno = es_gobierno

    def calcular_valor_compra(self):
        valor_por_metro_cuadrado = 3500000
        return self._area * valor_por_metro_cuadrado

    def imprimir(self):
        super().imprimir()
        print(f"Es gobierno: {'Sí' if self._es_gobierno else 'No'}")


# Prueba de escritorio
casa_rural = CasaRural(70343, 80, "Avenida Grande", 2, 2, 10, 1000)
local_comercial = LocalComercial(82343, 150, "Centro Comercial", "Zona Comercial", "CC Mall")
oficina = Oficina(93443, 200, "Edificio Corporativo", True)

casa_rural.imprimir()
print("--------------------------------------")
local_comercial.imprimir()
print("--------------------------------------")
oficina.imprimir()

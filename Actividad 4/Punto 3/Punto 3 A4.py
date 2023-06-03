class Animal:
    def __init__(self, sonidos, alimentos, hábitat, nombre_científico):
        self.sonidos = sonidos
        self.alimentos = alimentos
        self.hábitat = hábitat
        self.nombre_científico = nombre_científico

    def get_nombre_científico(self):
        return self.nombre_científico

    def get_sonido(self):
        return self.sonidos

    def get_alimentos(self):
        return self.alimentos

    def get_hábitat(self):
        return self.hábitat


class Cánido(Animal):
    pass


class Felino(Animal):
    pass


class Perro(Cánido):
    def __init__(self):
        super().__init__("ladrido", "carnívora", "doméstico", "Canis lupus familiaris")


class Lobo(Cánido):
    def __init__(self):
        super().__init__("aullido", "carnívora", "bosque", "Canis lupus")


class León(Felino):
    def __init__(self):
        super().__init__("rugido", "carnívora", "pradera", "Panthera leo")


class Gato(Felino):
    def __init__(self):
        super().__init__("maullido", "ratones", "doméstico", "Felis silvestris catus")


animales = [Gato(), Perro(), Lobo(), León()]

for animal in animales:
    print("Nombre científico:", animal.get_nombre_científico())
    print("Sonido:", animal.get_sonido())
    print("Alimentos:", animal.get_alimentos())
    print("Hábitat:", animal.get_hábitat())
    print()

class Forma():
    
    def area():
        pass


class Quadrado(Forma):
    
    # método construtor
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2


class Circulo(Forma):
    
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * self.raio ** 2

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

circulo = Circulo(5)
area_circulo = circulo.area()
print(area_circulo)


"""
A classe base Forma define a interface comum (area) que todas as formas devem implementar.
A classe Quadrado, Circulo implementam essa interface de maneira diferente, de acordo com suas características específicas.
No final, conseguimos tratar diferentes objetos (Quadrado, Retangulo, ...) da mesma maneira, iterando sobre eles e chamando o método area.
"""
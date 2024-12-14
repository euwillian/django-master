class Forma():
    
    def area():
        pass


class Quadrado(Forma):
    
    # método construtor
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)


"""
A classe base Forma define a interface comum (area) que todas as formas devem implementar.
A classe Quadrado implementam essa interface de maneira diferente, de acordo com suas características específicas.
No final, conseguimos tratar diferentes objetos (Quadrado, Retangulo, ...) da mesma maneira, iterando sobre eles e chamando o método area.
"""
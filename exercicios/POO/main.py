""" 
Programação orientada a objetos
"""
# Classe base
class Motor:
    combustivel = "Flex"
    litros = 48
    
    def ligar_carro(self):
        print('ligar carro..')
    
    
    def desligar_carro(self):
        print('desligar carro..')
        
        
    def acelerar(self):
        print('acelerando..')
    
    
    def frear(self):
        print('freando..')


# Herança - Herdar de outras classes, para evitar retrabalho, trabalho duplicado
class Carro(Motor):
    marca = 'Audi'
    modelo = 'Audi TT'
    ano = '2024'
    cor = 'Preto'
    portas = 4
    
    def limpador(self):
        print('ligar limpador..')

    
    def ligar_musica(self):
        print('ligar musica..')
    
    
    def piloto_automatico(self):
        print('acionar piloto automático..')
    
    # Essa função é um polimorfismo pois, existe na classe Motor, mas eu adicionei mais coisas nela
    def desligar_carro(self):
        print('desligar carro..')
        print('Desligando outros componentes específicos.. ')
        

carro = Carro()
carro.ligar_carro()
carro.desligar_carro()
print(carro.combustivel)
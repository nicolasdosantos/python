#Classe Pessoa: Crie uma classe que modele uma pessoa:
#a. Atributos: nome, idade, peso e altura
#b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer
#0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def Envelhecer(self,idade):
        self.idade = idade
        if (self.idade < 21):
            self.crescer(0.5)
    def Engordar(self,idade):
        pass  
class Celular:

    def __init__(self,marca,modelo):

        self.marca=marca
        self.modelo=modelo
        self.bateria=100

    def fazer_ligacao(self, minutos):
        consumo=minutos * 2
        self.bateria=self.bateria-consumo

        print(f"efetuando ligacao de {minutos} minutos do meu {self.modelo}")  
        print(f"bateria restante: {self.bateria} %")

meu_celular=Celular("Samsung", "m34")

print(f"Meu celular e um {meu_celular.marca} {meu_celular.modelo}")
print(f"Bateria inicial: {meu_celular.bateria} %")

meu_celular.fazer_ligacao(10)

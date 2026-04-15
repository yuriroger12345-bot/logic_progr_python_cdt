'''
class Carro:
    # Todo: Test this method
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    # Todo: Test this method
    def buzinar(self):
        print(f'O {self.marca} da cor {self.cor} fez Bip Bip!')

meu_carro = Carro('Toyota', 'cinza')
carro_do_cliente = Carro('Honda', 'preto')

meu_carro.buzinar()
carro_do_cliente.buzinar()

exerxicio pratico
simule um carregamento de um celular quando estiveer 5% de bateria mensagem aviso e com 85% avise que esta carregado
'''
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False
        self.bateria = 100
def ligar(self):
        self.ligado = True
        print(f'{self.marca} {self.modelo} ligado.')
  
def carregar(self):
    self .bateria =100
    print(f'{self.marca} {self.modelo} carregado.') 
meu_celular = Celular('Samsung', 'Galaxy S21')
meu_celular.ligar()
meu_celular.bateria=5
print
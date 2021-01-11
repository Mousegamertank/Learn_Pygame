import objetos_e_personagens as obp

class configuracao_de_texto():
    def __init__(self, Estilo, Tamanho):
        self.Estilo = Estilo
        self.Tamanho = Tamanho

fonte1 = configuracao_de_texto(None, 55)

# Guardar os textos que será apresentados
Textos = {
    'Teste' : 'TESTE1',
    'Win' : 'Congratulation!! You Win!!',
    'Lose' : 'You Lose!!! '
    }


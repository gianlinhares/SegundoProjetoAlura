from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(Self, nome, categoria):
        Self._nome = nome.title()
        Self._categoria = categoria.upper()        
        Self._ativo = False
        Self._avaliacao = []
        Restaurante.restaurantes.append(Self)

    def __str__(self):
        return f'{self._nome.ljust(25)}|{self._categoria.ljust(25)}|{self.media_avaliacoes.ljust(25)}|{self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)}|{'Categoria'.ljust(25)}|{'Avaliação'.ljust(25)}|{'Status'}')
        for restaurante in cls.restaurantes:
            print(restaurante)

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'
    
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: # se nota estiver entre 0 e 5
                avaliacao = Avaliacao(cliente, nota)
                self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem Avaliações'        
        total = sum(avaliacao._nota for avaliacao in self._avaliacao)
        return str(round(total / len(self._avaliacao), 1))

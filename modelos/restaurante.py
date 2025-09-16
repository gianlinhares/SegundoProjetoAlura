class Restaurante:

    restaurantes = []

    def __init__(Sefl, nome='', categoria=''):        
        Sefl.nome = nome
        Sefl.categoria = categoria
        Sefl.ativo = False
        Restaurante.restaurantes.append(Sefl)

    def __str__(self):
        return f'Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(restaurante)
    
restaurante_subway = Restaurante('Subway', 'Fast Food')
restaurante_minato = Restaurante('Minato', 'Comida Japonesa')

Restaurante.listar_restaurantes()
from modelos.restaurante import Restaurante

restaurante_subway = Restaurante('Subway', 'Sanduíches')
restaurante_subway.receber_avaliacao('Gianluca', 10)
restaurante_subway.receber_avaliacao('João', 8)
restaurante_subway.receber_avaliacao('Maria', 2)

def main(): 
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
class Pessoa:

    def __init__(self, *filhos, nome = None):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá mundo'

if __name__ == '__main__':
    afonso = Pessoa(nome='Afonso')
    alisson = Pessoa(afonso, nome='Alisson')

    print(alisson.filhos)
    for filho in afonso.filhos:
        print(filho.nome)
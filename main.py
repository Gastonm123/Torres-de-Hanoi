#crear una clase que maneje las torres y tenga metodos para ganar
from __future__ import print_function

def mostrar(juego):
    for i, torre in enumerate(juego.torres):
        print('Torre ' + str(i) + ': ', end='')
        for pieza in torre:
            print(str(pieza), end=', ') 
        print('')

class Juego:
    def __init__(self, nro_piezas):
        self.torres = [
            [nro_piezas-i for i in range(nro_piezas)],
            [],
            []
        ]
        self.piezas = [0 for i in range(nro_piezas)]
        self.graficador = None
        self.nro_piezas = nro_piezas

    def mover(self, pieza, torre, torreNegada=0):
        #conseguir la torre a la que lo voy a mover
        for i in range(3):
            if i != torre and i != torreNegada:
                torreMover = i
                break

        #mover la pieza de encima a otro lugar que no sea donde me voy a mover
        if pieza > 1:
            self.mover(pieza-1, torre, torreMover)
        
        #moverme
        self.torres[torre].pop()
        self.torres[torreMover].append(pieza)
        self.piezas[pieza-1] = torreMover
        if self.graficador:
            self.graficador.graf(self)
        else:
            mostrar(self)

        #recobrar el estado de la recursion poniendo la pieza que antes movi arriba mio
        if pieza > 1:
            self.mover(pieza-1, self.piezas[pieza-2], torre)

    def setGraficador(self, graficador):
        self.graficador = graficador

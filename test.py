from __future__ import print_function
from main import Juego
from graficador import Graficador

def mostrar(juego):
    for i, torre in enumerate(juego.torres):
        print('Torre ' + str(i) + ': ', end='')
        for pieza in torre:
            print(str(pieza), end=', ') 
        print('')

g = Graficador()    
piezas = 7
miJuego = Juego(piezas)
miJuego.setGraficador(g)

g.graf(miJuego)
miJuego.mover(piezas, 0)
while(1):
    g.graf(miJuego)

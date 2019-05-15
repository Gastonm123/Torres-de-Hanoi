from __future__ import print_function
from main import Juego

def mostrar(juego):
    for i, torre in enumerate(juego.torres):
        print('Torre ' + str(i) + ': ', end='')
        for pieza in torre:
            print(str(pieza), end=', ') 
        print('')

    
piezas = 20
miJuego = Juego(piezas)

mostrar(miJuego)
miJuego.mover(piezas, 0)
mostrar(miJuego)
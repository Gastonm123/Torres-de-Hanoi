from main import Juego
from graficador import Graficador

g = Graficador()    
piezas = 7
miJuego = Juego(piezas)
miJuego.setGraficador(g)

g.graf(miJuego)
miJuego.mover(piezas, 0)
while(1):
    g.graf(miJuego)

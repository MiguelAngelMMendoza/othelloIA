from Tablero import * 


        
"recibe un tablero de juego"
def h1(self):
    puntuacionFinal = cantidadFichasNegras - cantidadFichasBlancas
    if(puntuacionFinal > 0):
        return 100 
    else:
        return -100    
    return puntuacionFinal

def cantidadFichasNegras(self):
    puntuacion = 0
    for i in range(self.dimension):
            for j in range(self.dimension):
                if self.mundo[i][j] == 1:
                    puntuacion = puntuacion + 1
        return puntuacion
    
def cantidadFichasBlancas(self):
    puntuacion = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.mundo[i][j] == 2:
                    puntuacion = puntuacion + 1
        return puntuacion    
    
    

import random
import time
import os
class Caballo(object):
    def __init__(self, name, f, t):
        self.name = name
        self.posicion = 0
        self.f = f
        self.t = t
    
    def corre(self):
        p = random.randint(self.f, self.t)
        self.posicion = self.posicion + p

    def dibuja(self):
        x = ("-" * self.posicion) + f"[{self.name}]"
        print(x)

pista = [
    Caballo("Yatasto", 1, 7), 
    Caballo("Pingo", 1, 6), 
    Caballo("Reina", 1, 5), 
    Caballo("Negrito", 1, 5), 
    Caballo("CocaCola", 1, 5), 
    Caballo("Alfajor", 1, 5)
]

termino = False
while termino == False:
    i = 0
    os.system("clear")
    while i < len(pista):
        pista[i].corre()
        pista[i].dibuja()
        if pista[i].posicion > 100:
            termino = True
        i = i + 1

    time.sleep(0.5)
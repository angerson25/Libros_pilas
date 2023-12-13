##Se requiere generar aleatoriamente un grupo de n libro de tres categorias (A,B,C), estos libros deben ser organizados para ser leidos , el ultimo libro para leer debe ser uno de categoria c y el primero uno de categoria a, si no existen libros de estas dos categorias se deben volver a generar los libros (implementacion en phyton )

import random
libros=[]
categorias=["A","B","C"]
catLibros=[]

while True:
    try:
        n = int(input("Por favor, ingresa un número mayor que 0: "))
        if n > 0:
            break  # Sal del bucle si el número es válido
        else:
            print("El número debe ser mayor que 0. Intenta de nuevo.")
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

for i in range(n):
    numero=random.randint(1, 3)
    libros.append(numero)
    
print(libros) 
    
for x in libros:
    catLibros.append(categorias[x-1])

print(catLibros)

class PilaDeLibros:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, libro):
        self.items.append(libro)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía. No se pueden desapilar más libros.")

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("La pila está vacía.")

    def tamano(self):
        return len(self.items)

pilaLibros = PilaDeLibros()
for j in catLibros:
    ##Apilar los libros de c
    if j == "C":
        pilaLibros.apilar(j)
        
        
if pilaLibros.esta_vacia():
    print("No hay libros de categoria C")    

else:   
    for k in catLibros:
        if k == "B":
            pilaLibros.apilar(k)
    
          
    for l in catLibros:
        if l == "A":
            pilaLibros.apilar(l)


print("\nFila apilada\n",pilaLibros.items)     
    
    
        
        

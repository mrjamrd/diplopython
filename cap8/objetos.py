"""
Programacion orientada a objeto
"""
#definir una clase
class Coche:
    #Artibutos o propiedades
    #caratectistica del coche

    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    #Medotos son las acciones que hace el objeto coche (funciones)
    def setMarca(self,marca):
        self.marca = marca
    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad +=1
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    def setColor(self,color):
            self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo(self):
        return self.modelo

#Fin de dificion de clase

#Crear un objeto  / Instanciar la clase
coche  = Coche()
print(coche.marca, coche.color)

print("Velociddad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

coche.setColor("rojo")
print(coche.getColor())

coche.setModelo("Camry")
print(coche.getModelo())

print("velocidad Nueva: ", coche.getVelocidad())

coche2 = Coche()

coche2.setMarca("Toyota")
print(coche2.getMarca())
coche2.setModelo("Corolla")
print(coche2.getModelo())

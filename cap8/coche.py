class Coche:
    #Artibutos o propiedades
    #caratectistica del coche

    color = "rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    def __init__(self,color,marca, modelo, velocidad, caballaje, plaza):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plaza = plaza

# Herencia: Es la posibilidad de compartir atributos y metodos

# Entre clases. Y que diferentes clases hereden de otras
class Persona:
    """
    nombre
    apellidos
    alturas
    edad
    """
    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.getApellidos

    def getAltura(self):
        return self.altura

    def getEdad(self):
        return self.edad

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidos(self,apellidos):
        self.apellidos = apellidos

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy dumiendo"

class Informatico(Persona):
    """"
    lenguaje
    experencia
    """
    def __init__(self):
        self.lenguaje = "html, css. javascript, php"
        self.experencia = 5
    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguaje):
        self.lenguaje = lenguaje

    def programar(self):
        return "Estoy Programando"

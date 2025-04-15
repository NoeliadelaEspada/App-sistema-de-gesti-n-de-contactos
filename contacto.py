
class Contacto:
    def __init__(self, nombre="", numero=None, correo=""):
        self.nombre = nombre
        self.numero = numero
        self.correo = correo

    def __str__(self):
        return f'Nombre: {self.nombre}, Número de teléfono: {self.numero}, Correo electrónico: {self.correo}'
    
        
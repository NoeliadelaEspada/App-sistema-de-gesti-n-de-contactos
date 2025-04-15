import os.path
from contacto import Contacto

class GestionContactos:
    
    def __init__(self):
       self.contactos = []       
       self.documentolista = 'listacontactos.txt'
   
       if os.path.isfile(self.documentolista): 
        self.contactos = self.leer_contactos_archivo()
       else:
        self.crear_lista_inicial()

    def leer_contactos_archivo(self):
        contactos = []
        with open(self.documentolista, 'r', encoding='utf8') as archivo:
            for linea in archivo:
              datos = linea.strip().split(', ')
              if len(datos) == 3:
                  nombre = datos[0].replace('Nombre: ', '')
                  numero = datos[1].replace('Numero de teléfono: ', '')
                  correo = datos[2].replace('Correo electrónico: ', '')
                  contactos.append(Contacto(nombre, numero, correo))
        return contactos  
        
    def crear_lista_inicial(self):
        contactos_iniciales = [ 
            Contacto('María Jimenez', 4593373, 'maria_jimenez25@hotmail.com'),    
            Contacto('Clara Lago', 3444576, 'claralago5@gmail.com'), 
            Contacto('Sara Pérez', 7842211, 'saritapereez10@hotmail.com'), 
        ]
        self.contactos.extend(contactos_iniciales) 
        for contacto in contactos_iniciales:
            self.agregarContacto(contacto) 
    
    def agregarContacto(self, contacto):
        try:
            with open(self.documentolista, 'a', encoding='utf8') as archivo:
                archivo.write(f'Nombre: {contacto.nombre}, Numero de teléfono: {contacto.numero}, Correo electrónico: {contacto.correo}\n')
            
        except Exception as e:
           print(f'Se ha producido un error de tipo {e}')

    def mostrarContactos(self):
        with open(self.documentolista, 'r', encoding='utf8') as archivo:
           print('|Lista de contactos|')
           print(archivo.read())

    def buscarContacto(self):
        contacto_buscar = input('Introduce el contacto que deseas buscar: ') 
        encontrado = False
        try:
           with open(self.documentolista, 'r', encoding='utf8') as archivo:
                for linea in archivo:
                   if contacto_buscar.lower() in linea.lower():
                      print(f'Se ha encontrado el contacto {contacto_buscar} en la línea: {linea.strip()}.')
                      encontrado= True
                if not encontrado:
                      print(f'El contacto {contacto_buscar} no se encuentra en la lista')
        except Exception as e:
           print(f'Ocurrió un error de tipo {e} al buscar el contacto.')
                
                      
    def eliminarContacto(self):
        contacto_eliminar = input('Introduzca el nombre, número o correo electrónico del contacto que desea eliminar: ')
        try:
            with open(self.documentolista, 'r', encoding='utf8') as archivo:
                lineas = archivo.readlines()

            lineas_corregidas = [linea for linea in lineas if contacto_eliminar.lower() not in linea.lower()]
            if len(lineas_corregidas) < len(lineas):
                with open(self.documentolista, 'w', encoding='utf8') as archivo:
                     archivo.writelines(lineas_corregidas)
                print(f'El contacto {contacto_eliminar} se ha eliminado correctamente.')
            else:
                print(f'El contacto {contacto_eliminar} no se encuentra en la lista.')
        except Exception as e:
           print('Se ha producido un error al eliminar el contacto.')
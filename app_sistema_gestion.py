from GestionContactos import GestionContactos
from contacto import Contacto
import re

class App_gestion_contactos:
    def __init__(self):
        self.gestion_contactos = GestionContactos()

    def correo_correcto(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

        return re.match(patron, correo)

    def mostrar_menu(self):
        while True:
            try:
                print('''
                        |MENU DE OPCIONES|
                        1. Agregar un contacto al sistema.
                        2. Mostrar lista de contactos.
                        3. Buscar contacto.
                        4. Eliminar contacto de la lista.
                        5. Salir''')
                seleccion = int(input('Por favor, introduce una opción (1-5): '))
                
                if seleccion == 1:
                        nombre_contacto = input('Por favor, introduce el nombre del contacto: ')
                        numero_contacto = int(input('Por favor, introduce el número de contacto: '))
                        while True:
                            try:
                                correo_electronico = input('Por favor, introduce un correo electrónico: ')
                                if self.correo_correcto(correo_electronico):
                                    break
                                else:
                                    raise ValueError('El correo electrónico introducido no es válido, revisa el formato.')
                            except ValueError as e:
                             print(f'Ha ocurrido un error de tipo {e} inténtalo de nuevo.')

                        contacto = Contacto(nombre_contacto, numero_contacto, correo_electronico)
                        self.gestion_contactos.agregarContacto(contacto)
                        print('El nuevo contacto ha sido agregado a tu lista de contactos. ')
                
                elif seleccion == 2:
                     self.gestion_contactos.mostrarContactos()

                elif seleccion == 3:
                    self.gestion_contactos.buscarContacto()
            
                elif seleccion == 4:
                    self.gestion_contactos.eliminarContacto()

                elif seleccion == 5:
                    print('¡Hasta pronto! Salimos de la aplicación')
                    break
                else:
                    print(f'La opción seleccionada {seleccion} no es válida, pruebe con otra opción.')
                     
            except ValueError:
                print(f'Error. Introduzca un número válido.')

            except Exception as e:
                print(f'Ocurrió un error inesperado: {e}')



if __name__ == '__main__':
    app_gestion = App_gestion_contactos()
    app_gestion.mostrar_menu()
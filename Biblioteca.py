import json

from Libro import Libro


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, id):
        for libro in self.libros:
            if libro.id == id:
                return libro
        return None

    def actualizar_libro(self, id, nuevo_titulo, nuevo_autor, nuevo_año):
        libro = self.buscar_libro(id)
        if libro:
            libro.titulo = nuevo_titulo
            libro.autor = nuevo_autor
            libro.año = nuevo_año
            print("Libro actualizado con éxito.")
        else:
            print("Libro no encontrado.")

    def eliminar_libro(self, id):
        libro = self.buscar_libro(id)
        if libro:
            self.libros.remove(libro)
            print("Libro eliminado")
        else:
            print("No se pudo encontrar el libro")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros")
        else:
            for libro in self.libros:
                libro.mostrar_informacion()

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            libros_json = [libro.__dict__ for libro in self.libros]
            json.dump(libros_json, f)
            print("Datos guardados con éxito")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                libros_json = json.load(f)
                self.libros = [Libro(libro['id'], libro['titulo'], libro['autor'], libro['año']) for libro in
                               libros_json]
            print("Datos cargados desde el archivo.")
        except FileNotFoundError:
            print("El archivo no existe.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON.")


def menu():
    print("\n============== Menú ==============")
    print("1. Agregar libro")
    print("2. Actualizar libro")
    print("3. Buscar libro")
    print("4. Eliminar libro")
    print("5. Mostrar libros")
    print("6. Guardar en archivo")
    print("7. Cargar desde archivo")
    print("8. Salir")


if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            id = input("Ingrese el ID del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            año = input("Ingrese el año de publicación del libro: ")
            libro = Libro(id, titulo, autor, año)
            print("---------------------------------------")
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            id = input("Ingrese el ID del libro a actualizar: ")
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_autor = input("Ingrese el nuevo autor del libro: ")
            nuevo_año = input("Ingrese el nuevo año de publicación del libro: ")
            print("---------------------------------------")
            biblioteca.actualizar_libro(id, nuevo_titulo, nuevo_autor, nuevo_año)

        elif opcion == "3":
            id = input("Ingrese el ID del libro a buscar: ")
            libro = biblioteca.buscar_libro(id)
            if libro:
                print("---------------------------------------")
                libro.mostrar_informacion()
            else:
                print("---------------------------------------")
                print("Libro no encontrado.")

        elif opcion == "4":
            id = input("Ingrese el ID del libro a eliminar: ")
            print("---------------------------------------")
            biblioteca.eliminar_libro(id)

        elif opcion == "5":
            print("---------------------------------------")
            biblioteca.mostrar_libros()

        elif opcion == "6":
            archivo = input("Ingrese el nombre del archivo para guardar: ")
            print("---------------------------------------")
            biblioteca.guardar_en_archivo(archivo)

        elif opcion == "7":
            archivo = input("Ingrese el nombre del archivo para cargar: ")
            print("---------------------------------------")
            biblioteca.cargar_desde_archivo(archivo)

        elif opcion == "8":
            break

        else:
            print("---------------------------------------")
            print("Opción inválida. Por favor, ingrese un número del 1 al 8.")

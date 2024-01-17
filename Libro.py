class Libro:
    def __init__(self, id, titulo, autor, año):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrar_informacion(self):
        print(f"ID: {self.id}\n"
              f"Título: {self.titulo}\n"
              f"Autor: {self.autor}\n"
              f"Año: {self.año}\n")
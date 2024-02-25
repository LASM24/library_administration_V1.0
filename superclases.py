""" Clases bases para el fincionamiento del programa """
# importacion para tipado
from typing import List


# clase libro
class Book:
    # inicializacion de los atributos de la clase
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

    # metodo para mostrar info del libro
    def print_info(self) -> None:
        print(f'Título: {self.title}, Autor: {self.author}, \
Año de publicación: {self.year}')


# clase biblioteca en donde se crean los metodos necesarios
class Library:
    # array para guardar los libros
    def __init__(self) -> None:
        self.books: List[Book] = []

    # metodo para añadir un libro
    def add_book(self, book: Book) -> None:
        self.books.append(book)

    # metodo para prestar un libro
    def lend_book(self, title: str) -> str:
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                found = True
                print('Libro encontrado:')
                book.view_info()
                self.books.remove(book)
                print('Libro prestado exitosamente')
                break
        if not found:
            print('Libro no encontrado en la biblioteca')

    # metodo para ver los libros guardados
    def show_books(self) -> None:
        print('Libros disponibles:')
        for book in self.books:
            book.view_info()

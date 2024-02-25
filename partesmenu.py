# importacion de clases
from superclases import Book, Library
# importaciones para limpiar la pantalla
import os
# importacion para tipado
from typing import Optional


# funcion para limpiar consola y que se vea bonito :3
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# menu inicial
def menu_base() -> int:
    while True:
        try:
            clear_console()
            res = int(input("Que desea realizar?\n"
                            "1. Ver libros disponibles.\n"
                            "2. Agregar libros.\n"
                            "3. Prestar libro.\n"
                            "4. Devolver libros.\n"
                            "5. Salir\n"
                            "Seleccione una opción:  "))
            if res in range(1, 6):
                return res
            else:
                raise ValueError('Opción no válida')
        except ValueError:
            print('Debe ingresar un número entero entre 1 y 5.')
            input('Presione enter para continuar...')


# opciones del menu y uso de las clases
def menu(library: Library) -> Optional[bool]:
    r = menu_base()
    if r == 1:
        clear_console()
        library.show_books()
        print()
        input('Presione enter para continuar...')
    elif r == 2:
        clear_console()
        title = str(input('Inserte título del libro: '))
        author = str(input('Inserte autor del libro: '))
        year = int(input('Inserte año de publicación del libro: '))
        book = Book(title, author, year)
        library.add_book(book)
        clear_console()
        print('Información del libro:')
        book.view_info()
        print('Libro añadido satisfactoriamente')
        print()
        input('Presione enter para continuar...')
    elif r == 3:
        clear_console()
        title = str(input('Inserte título del libro a prestar: '))
        library.lend_book(title)
        print()
        input('Presione enter para continuar...')
    elif r == 4:
        clear_console()
        print('Información del libro:')
        title = str(input('Inserte título del libro: '))
        author = str(input('Inserte autor del libro: '))
        year = int(input('Inserte año de publicación del libro: '))
        book = Book(title, author, year)
        library.add_book(book)
        clear_console()
        print('Información del libro:')
        book.view_info()
        print('Libro devuelto satisfactoriamente')
        print()
        input('Presione enter para continuar...')
    elif r == 5:
        clear_console()
        print('Regrese pronto :D')
        return False
    return True

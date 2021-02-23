""" 
        Concerned with storing and retreiving books from the list
"""

books = []

def add_book(name, author):
    books.append({'name':name, 'author':author, 'read': False})
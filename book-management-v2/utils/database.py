import json

""" 
        Concerned with storing and retreiving books from the list
"""

books_file = 'books.json'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)

def add_book(name, author):
    books = get_all_books()
    books.append({'name':name, 'author':author, 'read':False})
    _save_all_books_(books)

def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books_(books):
    with open (books_file, 'w') as file:
        json.dump(books, file)



def mark_book_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True
        _save_all_books_(books)


def delete_book(name):
    books = get_all_books() 
    books = [book for book in books if book['name'] != name]#add each book to new books list if name is not equal to the name that needs to be deleted
    _save_all_books_(books)
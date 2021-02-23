""" 
        Concerned with storing and retreiving books from the list
"""

books = []

def add_book(name, author):
    books.append({'name':name, 'author':author, 'read': False})


def get_all_books():
    return books


def mark_book_read(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True

def delete_book(name):
    global books 
    books = [book for book in books if book['name'] != name] #add each book to new books list if name is not equal to the name that needs to be deleted
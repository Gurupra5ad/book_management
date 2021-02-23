from utils import database

USER_CHOICE = """
Enter :
 - 'a' to add a new book
 - 'l' to list all the books
 - 'r' to remove a book
 - 'd' to delete a book
 - 'q' to quit 
Your choice ? : """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass

#def prompt_add_book() ask for book name and add a book
#def list_books() show all the books in our list
#def promp_read_book() ask for book name and modify it to read in our list 
#def remove_book() ask for book name and delete it from our list
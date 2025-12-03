# Name: Inthat # Student ID: 68010545999

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library():
    def __init__(self):
        self.__book = []

    def add_book(self, title, author):
        newbook = Book(title, author)
        self.__book.append(newbook)
    
    def get_book_count(self):
        return len(self.__book)

    def display_books(self):
        book_list = []
        for b in self.__book:
            book_list.append(f'{b.title} by {b.author}')
        return book_list
library = Library()
while True:
    command = input("Command (add/view/count/exit): ")
    if command.lower == 'exit':
        print("Goodbye")
        break
    elif command.lower() == 'add':
        title = input("Enter title: ")
        author = input("Enter Author: ")
        library.add_book(title, author)

        print('Book added.')
    elif command.lower() == 'view':
        print('--- Library Holdings ---')
        for i in (library.display_books()):
            print(i)
        print('------------------------')
    elif command.lower() == 'count':
        print(f"Book count: {library.get_book_count()}")
    else:
        print('Input error.')
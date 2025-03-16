class Library:
    def __init__(self):
        self.book_list = []        

    def register_book(self, book_name):
        # Cria um dicionário para cada livro e adiciona à lista
        book = {
            'book name': book_name,
            'is available': True
        }
        self.book_list.append(book)

    def lend(self, book_name):
        for book in self.book_list:
            if book['book name'] == book_name and book['is available']:
                book['is available'] = False
                print(f"The book '{book_name}' was lent.")
                return
        print(f"The book '{book_name}' is not available for lending.")

    def give_back(self, book_name):
        for book in self.book_list:
            if book['book name'] == book_name and not book['is available']:
                book['is available'] = True
                print(f"The book '{book_name}' was returned.")
                return
        print(f"The book '{book_name}' was already returned or not found.")
    
    def show_books(self):
        if not self.book_list:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.book_list:
                status = "Available" if book['is available'] else "Not Available"
                print(f"- {book['book name']} ({status})")

library = Library()

library.register_book('Livro 1')
library.register_book('Livro 2')

library.show_books()

library.lend('Livro 1')

library.lend('Livro 1')

library.give_back('Livro 1')

library.give_back('Livro 1')

library.show_books()

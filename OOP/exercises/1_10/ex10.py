class Book():
    def __init__(self, book_title, book_author, PAGES):
        self.title = book_title
        self.author = book_author
        self.PAGES = PAGES
        self.available = True

    def lend(self):
        if self.available:
            self.available = False
            return
        return print(f'The book {self.title} is not available for lending')
    
    def give_back(self):
        if not self.available:
            self.available = True
            return 
        return print(f'The book {self.title} was already given back.')

book1 = Book('Periféricos', 'William Gibson', 1)

book1.lend()
book1.give_back()
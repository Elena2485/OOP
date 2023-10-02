

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print('Книга находится у абонента')
        else:
            self.checked_out = True
            print('Выдаем книгу абоненту')


    def check_in(self):
        if not self.checked_out:
            print('Книга в наличии')
        else:
            self.checked_out = False
            print('Принимаем книгу в библиотеку')

book1 = Book('Война и мир', 'Л. Н. Толстой')



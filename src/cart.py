class Cart:

    _books = 0

    def get_bill(self):
        if self._books > 0:
            return 8
        return 0

    def add_a_book(self):
        self._books += 1

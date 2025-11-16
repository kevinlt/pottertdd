from src.purchased_book import PurchasedBook
from src.cart import Cart


class TestBuyingBooks:

    def test_should_return_0_if_no_books_to_buy(self):
        cart = Cart()
        assert cart.get_bill() == 0

    def test_should_return_8_if_cart_has_1_book(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).build())
        assert cart.get_bill() == 8

    def test_should_return_16_if_cart_has_2_books(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).quantity(2).build())
        assert cart.get_bill() == 16

    def test_should_return_5_percent_discount_when_cart_has_2_different_books(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).build())
        cart.add_a_book(BookBuilder().of_id(2).build())

        assert cart.get_bill() == 16 * 0.95

class BookBuilder:

    _id: int = 0
    _name: str = ""
    _price: float = 8.0
    _quantity: int = 1

    def build(self):
        return PurchasedBook(self._id, self._name, self._price, self._quantity)

    def of_id(self, id: int):
        self._id = id
        return self

    def quantity(self, quantity: int):
        self._quantity = quantity
        return self
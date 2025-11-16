from src.purchased_book import PurchasedBook
from src.cart import Cart


class TestBuyingBooks:

    _discount_dataset = [
        (1, [1,2], 8 * 2 * 0.95),
        (1, [1,2,3], 8 * 3 * 0.9),
        (1, [1,2,3,4], 8 * 4 * 0.85),
        (1, [1,2,3,4,5], 8 * 5 * 0.8),
        (1, [1,2,3,4,5,6], 8 * 6 * 0.75),
        (1, [1,2,3,4,5,6,7], 8 * 7 * 0.7)
    ]

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

    def test_should_apply_discount_when_cart_has_different_books(self):
        for book_quantity, ids, expected_bill in self._discount_dataset:
            cart = Cart()
            for id in ids:
                cart.add_a_book(BookBuilder().of_id(id).quantity(book_quantity).build())
            assert cart.get_bill() == expected_bill

    def test_should_apply_discount_only_on_first_batched_books(self):
        cart = Cart()
        cart.add_a_book(BookBuilder().of_id(1).quantity(2).build())
        cart.add_a_book(BookBuilder().of_id(2).quantity(1).build())
        assert cart.get_bill() == 2 * 8 * 0.95 + 1 * 8

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
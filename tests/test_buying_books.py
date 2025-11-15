from src.cart import Cart


class TestBuyingBooks:

    def test_should_return_0_if_no_books_to_buy(self):
        cart = Cart()
        assert cart.get_bill() == 0

    def test_should_return_8_if_cart_has_1_book(self):
        cart = Cart()
        cart.add_a_book()
        assert cart.get_bill() == 8
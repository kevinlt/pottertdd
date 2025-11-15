from src.cart import Cart


class TestBuyingBooks:

    def test_should_return_0_if_no_books_to_buy(self):
        cart = Cart()
        assert cart.get_bill() == 0
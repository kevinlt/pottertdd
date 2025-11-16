class PurchasedBook:

    id: int
    title: str
    price: float
    quantity: int

    def __init__(self, id: int, title: str, price: float, quantity: int = 1):
        self.id = id
        self.title = title
        self.price = price
        self.quantity = quantity
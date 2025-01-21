import json
from products import Product, get_product
from cart import dao


class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict) -> "Cart":
        return Cart(
            id=data["id"],
            username=data["username"],
            contents=data["contents"],
            cost=data["cost"],
        )


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = [
        item
        for cart_detail in cart_details
        for item in json.loads(cart_detail["contents"])  # Use json.loads instead of eval for safety.
    ]
    return [get_product(item) for item in items]


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
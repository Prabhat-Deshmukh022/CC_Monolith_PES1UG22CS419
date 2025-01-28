import json
from products import Product
from cart import dao
import products

class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data):
        return Cart(data['id'], data['username'], data['contents'], data['cost'])


def get_cart(username: str) -> list:
    # Retrieve cart details from the database
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Flatten all product IDs from the cart details
    product_ids = [
        item for cart_detail in cart_details
        for item in json.loads(cart_detail['contents'])
    ]

    if not product_ids:
        return []

    # Use a batch query to get all product details at once
    products_details = get_products(product_ids)

    return products_details


def add_to_cart(username: str, product_id: int):
    # Directly call DAO for insertion
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    # Directly call DAO for removal
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    # Directly call DAO for deletion
    dao.delete_cart(username)

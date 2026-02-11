from __future__ import annotations
import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: tuple[int, int]
    products: dict[str, int | float]

    def customer_bill(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        total_purchase_cost = 0
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.products_to_buy.items():
            one_product_price = self.products[product] * quantity
            if isinstance(one_product_price, float) and one_product_price.is_integer():
                one_product_price = int(one_product_price)
            print(f"{quantity} {product}s for {one_product_price} dollars")
            total_purchase_cost += one_product_price
        print(f"Total cost is {total_purchase_cost} dollars")
        customer.money -= total_purchase_cost
        print("See you again!")

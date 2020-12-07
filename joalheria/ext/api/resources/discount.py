from .helper import discount_percent, minimum_amount_discount


class DiscountClient:
    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, product):
        if product.product_price >= minimum_amount_discount:
            return product.product_price * (discount_percent/100)
        return self.__next_discount.calculate(product)


class WithOutDiscount:
    def calculate(self, product):
        return 0

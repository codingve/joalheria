from .helper import (profit_percent,
                     profit_discount_percent,
                     minimum_amount_discount)


class ProfitWithDiscount:
    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calculate(self, product):
        if product.product_price >= minimum_amount_discount:
            return ((product.product_sale_price-product.product_commission) *
                    profit_discount_percent)/100

        return self.__next_discount.calculate(product)


class ProfitWithOutDiscount:
    def calculate(self, product):
        return ((product.product_sale_price-product.product_commission) *
                profit_percent)/100

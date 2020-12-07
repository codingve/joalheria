from flask_restful import Resource, reqparse, request
from .discount import DiscountClient, WithOutDiscount
from .profit import ProfitWithDiscount, ProfitWithOutDiscount
from .helper import commission_percent
from .helper import formatCurrency


class CalculateDiscount:
    def calculate(self, product):
        return DiscountClient(WithOutDiscount()).calculate(product)


class CalculateProfit:
    def calculate(self, product):
        return ProfitWithDiscount(ProfitWithOutDiscount()).calculate(product)


class Product(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, location='args',
                        help='This field (price) cannot be left blank')

    calculateDiscount = CalculateDiscount()
    calculateProfit = CalculateProfit()

    def __init__(self):
        data = Product.parser.parse_args()
        self.product_price = data["price"]
        self.product_discount = 0.0
        self.product_sale_price = 0.0
        self.product_commission = 0.0
        self.product_profit = 0.0

    # Getters
    @ property
    def product_discount(self):
        return self._product_discount

    @ product_discount.setter
    def product_discount(self, valor):
        self._product_discount = self.calculateDiscount.calculate(self)

    @ property
    def product_sale_price(self):
        return self._product_sale_price

    @ product_sale_price.setter
    def product_sale_price(self, valor):
        self._product_sale_price = (self.product_price - self.product_discount)

    @ property
    def product_commission(self):
        return self._product_commission

    @ product_commission.setter
    def product_commission(self, valor):
        self._product_commission = (self.product_sale_price *
                                    (commission_percent/100))

    @ property
    def product_profit(self):
        return self._product_profit

    @ product_profit.setter
    def product_profit(self, valor):
        self._product_profit = self.calculateProfit.calculate(self)

    def get(self):

        return {
            "gross_value": formatCurrency(self.product_price),
            "sale_discount": formatCurrency(self.product_discount),
            "sale_price": formatCurrency(self.product_sale_price),
            "commission": formatCurrency(self.product_commission),
            "profit": formatCurrency(self.product_profit)
        }

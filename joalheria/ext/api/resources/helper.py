import locale

discount_percent = 10
commission_percent = 5
profit_discount_percent = 30
profit_percent = 40
minimum_amount_discount = 5000.0


def formatCurrency(value):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    value = locale.currency(value, grouping=True, symbol=None)
    return value

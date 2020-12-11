# Jewelry shop
Calculate discounts, commission and profit of a jewelry shop

Docker build:
```sh
docker-compose up --build
```

Api documents:
```sh
http://localhost:5000/docs
```

Api tests:
```sh
pytest joalheria/tests/ -v --cov=joalheria
```

## REST API
| Endpoint | Método| Descrição |
|----------|--------|------------|
| /product?price=??? | GET  | Receive the product price (with dot for monetary separator) and return the discounts, commission and profit.|


#### Response (exemple price with discount):
```sh
{"gross_value": 9000.0, "sale_discount": 900.0, "sale_price": 8100.0, "commission": 405.0, "profit": 2308.5}
```

#### Response (exemple price with out discount):
```sh
{"gross_value": "856,99", "sale_discount": "0,00", "sale_price": "856,99", "commission": "42,85","profit": "325,66"}
```

NOTE:
Infelizmente não pude fazer todos os tratamentos que gostaria de fazer, quem sabe em uma próxima. Bye u all.

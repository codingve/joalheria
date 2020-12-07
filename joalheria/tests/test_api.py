# def test_api_is_online(client):
#     assert client.get("/").status_code == 200


def test_request_returns_404(client):
    assert client.get("/url_inexistente").status_code == 404


# def test_request_returns_200(client):
#     assert client.get("/product?price=9000").status_code == 200

def test_price(client):
    data_product = client.get('/product?price=90').get_json()

    assert data_product["price"] == "90"

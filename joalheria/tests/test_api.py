import requests
url = 'http://127.0.0.1:5000'


def test_api_is_online():
    assert requests.get(url+"/").status_code == 200


def test_request_returns_404():
    assert requests.get(url+"/url_inexistente").status_code == 404


def test_request_returns_200():
    assert requests.get(url+"/product?price=9000").status_code == 200


def test_request_blank():
    assert requests.get(url+"/product").status_code == 400


def test_request_blank_value():
    assert requests.get(url+"/product?price").status_code == 400


def test_request_string_value():
    assert requests.get(url+"/product?price=a").status_code == 400


def test_has_discount():
    r = requests.get(url+'/product?price=5000')
    data = r.json()

    assert r.status_code == 200
    assert data['sale_discount'] == "500,00"


def test_dont_has_discount():
    r = requests.get(url+'/product?price=500')
    data = r.json()

    assert r.status_code == 200
    assert data['sale_discount'] == "0,00"

from joalheria.app import minimal_app
from flask_restful import Api as FlaskRestful
from pytest import fixture


@fixture(scope="module")
def app():
    """Instance of minimal flask app"""
    return minimal_app()


@fixture
def flask_restful(mocker):
    """Instance mocker flask restful"""
    return mocker.MagicMock(spec=FlaskRestful)

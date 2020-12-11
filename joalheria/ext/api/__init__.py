from flask_restful import Api
from flask import make_response, jsonify
from .resources.product import Product


def init_app(app):
    api = Api(app)
    api.add_resource(Product, '/api/product', '/product')

    # @app.errorhandler(400)
    # def handle_400_error(_error):
    #     """Return a http 400 error to client"""
    #     return make_response(jsonify({'error': 'Misunderstood'}), 400)

    # @app.errorhandler(401)
    # def handle_401_error(_error):
    #     """Return a http 401 error to client"""
    #     return make_response(jsonify({'error': 'Unauthorised'}), 401)

    # @app.errorhandler(404)
    # def handle_404_error(_error):
    #     """Return a http 404 error to client"""
    #     return make_response(jsonify({'error': 'Not found'}), 404)

    # @app.errorhandler(500)
    # def handle_500_error(_error):
    #     """Return a http 500 error to client"""
    #     return make_response(jsonify({'error': 'Server error'}), 500)

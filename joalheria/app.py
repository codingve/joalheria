import os
from flask import Flask
from .ext import site
from .ext import api
from .docs import swagger


def minimal_app():
    app = Flask(__name__)

    return app


def create_app():
    app = minimal_app()
    site.init_app(app)
    api.init_app(app)
    swagger.init_app(app)

    return app


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=PORT, debug=False)

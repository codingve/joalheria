from flask_swagger_ui import get_swaggerui_blueprint


def init_app(app):
    SWAGGER_URL = '/docs'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Joalheria-Joia-Preciosa",
            'layout': "BaseLayout"
        }
    )

    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

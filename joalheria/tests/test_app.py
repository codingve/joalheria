def test_app_is_created(app_minimal):
    assert app_minimal.name == 'joalheria.app'


def test_config_is_loaded(config):
    assert config["DEBUG"] is False

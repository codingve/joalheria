clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build

# test:
# 	python -m unittest discover -v

# test pytest
test:
	pytest tests/ -v --cov=joalheria

install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install -r requirements_dev.txt
	pip install -r requirements_test.txt

run:
	FLASK_APP=joalheria/app.py flask run

run-dev:
	FLASK_APP=joalheria/app.py FLASK_ENV=development flask run
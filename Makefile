clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
	rm -fr docs/_build/
	rm -r .ipynb_checkpoints
	rm -r .pytest_cache
	rm -r .tests/__pycache__
	rm -r .pytest_cache


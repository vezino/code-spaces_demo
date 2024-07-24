install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt
		python -m textblob.download_corpora

test:
		# python -m pytest -vv --cov=hello --cov=greeting tests
		python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py

one-test:
		python -m pytest -vv tests/test_greeting.py::test_my_name4		

format:
		black *.py nlplogic

lint:	
		# pylint --disable=R,C hello.py
		pylint --disable=R,C *.py nlplogic/*.py

all: install lint test format

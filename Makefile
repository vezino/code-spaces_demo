install:
		pip install --upgrade pip &&\
		pip install -r requirements.txt
		python -m textblob.download_corpora

test:
		# python -m pytest -vv --cov=hello --cov=greeting tests
		# python -m pytest -vv --cov=wikiphrases --cov=nlplogic --cov=main test_corenlp.py
		python3.10 -m pytest -vv --cov=wikiphrases --cov=nlplogic --cov=main test_corenlp.py

one-test:
		# python -m pytest -vv tests/test_greeting.py::test_my_name4
		python3.10 -m pytest -vv tests/test_greeting.py::test_my_name4	

format:
		black *.py nlplogic

lint:	
		# pylint --disable=R,C hello.py
		pylint --disable=R,C *.py nlplogic/*.py
		#docker run --rm -i hadolint/hadolint < Dockerfile

all: install lint test format

# Use *-310 to run on cloud9

venv-310:
	python3.10 -m venv ~/.venv

install-310:
		pip3.10 install --upgrade pip &&\
		pip3.10 install -r requirements.txt
		python3.10 -m textblob.download_corpora

test-310:
		python3.10 -m pytest -vv --cov=wikiphrases --cov=nlplogic --cov=main test_corenlp.py

all-310: install-310 lint test-310 format

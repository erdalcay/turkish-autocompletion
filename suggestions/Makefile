# Makefile

development: venv requirements run

venv:
	# Create venv if it doesn't exist
	test -d venv || python3 -m venv venv;

requirements:
	# Install dependencies
	. venv/bin/activate; pip3 install -r requirements.txt

run:
	# Check if .flaskenv exists & run flask
	test -f .flaskenv && . venv/bin/activate && flask run || \
	echo ".flaskenv file must be present in the root directory"
# bfg-test

Set an environment variable
export VENV=~/bfg_test/env

Create a virtual environment
python3 -m venv $VENV

Update packaging tools in the virtual environment
$VENV/bin/pip install --upgrade pip setuptools

Install Pyramid
$VENV/bin/pip install "pyramid==1.10.2" waitress

Change folder
cd app

Install
$VENV/bin/pip install -e .
$VENV/bin/pip install -e ".[dev]"

Run the WSGI application with
$VENV/bin/pserve development.ini --reload
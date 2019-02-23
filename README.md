# Test task for [BFG Group](https://www.bfg-group.ru/)
## Web application to search for Stack Overflow


1. **Set an environment variable**

- export VENV=~/bfg_test/env

2. **Create a virtual environment**

- python3 -m venv $VENV

3. **Update packaging tools in the virtual environment**

- $VENV/bin/pip install --upgrade pip setuptools

4. **Install Pyramid**

- $VENV/bin/pip install "pyramid==1.10.2" waitress

5. **Change folder**

- cd app

6. **Install**

- $VENV/bin/pip install -e .
- $VENV/bin/pip install -e ".[dev]"

7. **Run this console script, thus producing our database and table**

- $VENV/bin/initialize_tutorial_db development.ini

8. **Run the WSGI application with**

- $VENV/bin/pserve development.ini --reload
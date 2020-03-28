Python School
=============

Elementary documents to study **Python**.
This series cover syntax, simple scripts, parsing various kind of data, and Web application.

Full HTML documents are available at:

* https://skitazaki.github.io/python-school-ja/

Setup
---------

Create a virtual Python environment with `venv`. ::

    $ pyvenv_dir=venv
    $ python3 -m venv $pyvenv_dir --prompt python-school-ja
    $ source $pyvenv_dir/bin/activate
    $ python3 -m pip install -U pip
    $ python3 -m pip install -r requirements.txt

Generate HTML documents. ::

    $ cd docs && make html && cd -

For scripts, install additional packages including local one. ::

    $ python3 -m pip install -e ".[dev,test]"

Edit
-----

Run web server which watches source files using ``livereload``. ::

    $ python3 -m pip install "livereload>=2.6"
    $ python3 docserver.py

Edit source documents under `docs/` directory.

If you edit Python scripts under `src/` directory, run a linter and a test runner. ::

    $ flake8 src/
    $ pytest src/

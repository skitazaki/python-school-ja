Python School
=============

Elementary documents to study **Python**.
This series cover syntax, simple scripts, parsing various kind of data, and Web application.

Full HTML documents are available at:

* http://skitazaki.github.com/python-school-ja/

Setup
---------

Create a virtual Python environment with `venv`. ::

    $ python3 -m venv $HOME/.pyvenv/python-school-ja
    $ source $HOME/.pyvenv/python-school-ja/bin/activate
    $ python3 -m pip install -U pip
    $ python3 -m pip install -r requirements.txt

Generate HTML documents. ::

    $ cd doc && make html

Edit
-----

Run web server which watches source files using ``livereload``. ::

    $ python3 -m pip install "livereload>=2.6"
    $ python3 docserver.py

Edit documents under `doc` directory.

Note
----

To update `gh-page`, save secure token via OAuth.

* `Sharing Travis-CI generated files`_

To write a script running on Travis-CI, be careful the difference between ``sh`` and ``bash``.

* `[ :Unexpected operator in shell programming`_

.. _`Sharing Travis-CI generated files`: http://sleepycoders.blogspot.jp/2013/03/sharing-travis-ci-generated-files.html
.. _`[ :Unexpected operator in shell programming`: http://stackoverflow.com/questions/3411048/unexpected-operator-in-shell-programming

About
-----

KITAZAKI Shigeru <skitazaki[at]gmail.com>

Python School
=============

Elementary documents to study **Python**.
This series cover syntax, simple scripts, parsing various kind of data, and Web application.

Full HTML documents are available at:

* http://skitazaki.github.com/python-school-ja/

Setup
---------

Create virtual Python environment with `pyvenv`. ::

    $ pyvenv $HOME/.pyvenv/python-school-ja
    $ source $HOME/.pyvenv/python-school-ja/bin/activate
    $ pip-3.3 install -r requirements.txt
    $ curl http://waf.googlecode.com/files/waf-1.7.13 >$HOME/.pyvenv/python-school-ja/bin/waf
    $ chmod +x $HOME/.pyvenv/python-school-ja/bin/waf
    $ waf configure

Optional to generate HTML documents using Python 2.7 ::

    $ virtualenv --distribute $HOME/.pyvenv/sphinx
    $ source $HOME/.pyvenv/sphinx/bin/activate
    $ pip install -r doc-requirements.txt
    $ cd doc
    $ make clean html

Above procedures are written in ``devsetup.sh``.

Edit
-----

Run web server which watches source files using ``livereload``. ::

    $ livereload -p 8000

Edit documents under `doc` directory.

Check syntax with ``flake8`` for Python 3.x syntax ::

    $ waf

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

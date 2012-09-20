Python School
=============
Elementary documents to study Python.
This series cover syntax, simple scripts, parsing various kind of data, and Web application.

Full HTML documents are available on github pages.

* http://skitazaki.github.com/python-school-ja/

Configure
---------
Setup Python environment with `virtualenv`. ::

    $ virtualenv --distribute .
    $ source bin/activate
    $ pip install -r requirements.txt

Optional::

    $ curl http://waf.googlecode.com/files/waf-1.7.2 >bin/waf
    $ chmod +x bin/waf

Optional::

    $ pip install -e git+git://github.com/michaeljones/sphinx-to-github.git#egg=sphinx-to-github

Build
-----
Compile reST documents. ::

    $ waf doc

Read
----
``doc/_build/html/index.html`` is your starting point.


ABOUT
-----
KITAZAKI Shigeru <skitazaki[at]gmail.com>


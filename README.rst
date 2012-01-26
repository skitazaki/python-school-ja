Python School
=============

Configure
---------
Setup Python environment with `virtualenv`. ::

    $ virtualenv --distribute .
    $ source bin/activate
    $ pip install -r requirements.txt

Optional::

    $ curl http://waf.googlecode.com/files/waf-1.6.8 >bin/waf
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


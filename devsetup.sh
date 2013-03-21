#!/bin/sh

BASEDIR=`cd $(dirname $0) && pwd`
VENV2="virtualenv --distribute"
VENV3=pyvenv
VENVDIR=$HOME/.pyvenv
SOURCE_VENVDIR=$VENVDIR/python-school-ja
DOC_VENVDIR=$VENVDIR/sphinx

WAF_VERSION=1.7.13

if [ ! -d $SOURCE_VENVDIR ]
then
    $VENV3 $SOURCE_VENVDIR
    source $SOURCE_VENVDIR/bin/activate
    curl -O http://python-distribute.org/distribute_setup.py
    python3 distribute_setup.py
    easy_install-3.3 pip
    pip-3.3 install -r requirements.txt
    curl http://waf.googlecode.com/files/waf-$WAF_VERSION >$SOURCE_VENVDIR/bin/waf
    chmod +x $SOURCE_VENVDIR/bin/waf
    waf configure
    rm distribute_setup.py distribute-*.tar.gz
fi

if [ ! -d $DOC_VENVDIR ]
then
    cd $BASEDIR/doc
    $VENV2 $DOC_VENVDIR
    source $DOC_VENVDIR/bin/activate
    pip install -r requirements.txt
    make clean html
    cd -
fi

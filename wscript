# -*- coding: utf-8 -*-

APPNAME = 'python-shool-ja'
VERSION = '2.0.0'

top = '.'
out = '_build'


def configure(ctx):
    ctx.find_program('flake8')
    ctx.find_program('nosetests')
    ctx.find_program('fab')


def build(bld):
    nodes = bld.path.ant_glob(['src/**/*py'],
                excl=['**/*.pyc', 'src/first-sample.py', '**/unicodecsv.py'])
    for node in nodes:
        bld(rule='${FLAKE8} --show-source ${TGT}', target=node)


def test(ctx):
    t = ctx.path.ant_glob(['src/csv-*.py', 'src/xml-*.py'],
            excl=['src/cmdline-*.py'])
    files = [f.abspath() for f in t]
    ctx.exec_command('nosetests -vv --with-xunit ' + ' '.join(files))


def dist(ctx):
    ctx.files = ctx.path.ant_glob(['doc/_build/html/**/*'])
    ctx.base_path = ctx.path.find_dir('doc/_build/html')

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :

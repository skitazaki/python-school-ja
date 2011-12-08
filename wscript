# -*- coding: utf-8 -*-

APPNAME = 'python-shool-ja'
VERSION = '1.0.0'

top = '.'
out = '_build'


def configure(ctx):
    ctx.find_program('pep8')
    ctx.find_program('pyflakes')
    ctx.find_program('sphinx-build')
    ctx.find_program('nosetests')


def build(bld):
    pass


def test(ctx):
    t = ctx.path.ant_glob('tests/*.py')
    files = [f.abspath() for f in t]
    ctx.exec_command('nosetests -vv ' + ' '.join(files))

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :

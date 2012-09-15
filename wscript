# -*- coding: utf-8 -*-

APPNAME = 'python-shool-ja'
VERSION = '1.3.0'

top = '.'
out = '_build'


def configure(ctx):
    ctx.find_program('pep8')
    ctx.find_program('pyflakes')
    ctx.find_program('sphinx-build')
    ctx.find_program('nosetests')
    ctx.find_program('fab')


def build(bld):
    nodes = bld.path.ant_glob(['src/**/*py'],
                excl=['**/*.pyc', 'src/first-sample.py', '**/unicodecsv.py'])
    for node in nodes:
        bld(rule='pep8 ${TGT}', target=node)
        bld(rule='pyflakes ${TGT}', target=node)


def doc(ctx):
    wd = 'doc'
    cmd = ['make', 'html']
    ctx.exec_command(cmd, cwd=wd)


def docclean(ctx):
    wd = 'doc'
    cmd = ['make', 'clean']
    ctx.exec_command(cmd, cwd=wd)


def test(ctx):
    t = ctx.path.ant_glob('src/csv-*.py',
            excl=['src/sphinx-to-github', 'src/cmdline-*.py'])
    files = [f.abspath() for f in t]
    ctx.exec_command('nosetests -vv --with-xunit ' + ' '.join(files))


def dist(ctx):
    ctx.algo = 'zip'
    ctx.files = ctx.path.ant_glob(['doc/_build/html/**/*'])
    ctx.base_path = ctx.path.find_dir('doc/_build/html')


def pages(ctx):
    ctx.exec_command('git checkout gh-pages')
    ctx.exec_command('cp -r doc/_build/html/* .')
    ctx.exec_command('git status')


# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :

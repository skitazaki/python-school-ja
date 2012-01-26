# -*- coding: utf-8 -*-

APPNAME = 'python-shool-ja'
VERSION = '1.1.0'

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
                excl=['**/*.pyc', 'src/ex01.py', '**/unicodecsv.py'])
    for node in nodes:
        bld(rule='pep8 ${TGT}', target=node)
        bld(rule='pyflakes ${TGT}', target=node)


def doc(ctx):
    wd = 'doc'
    cmd = ['make', 'html']
    ctx.exec_command(cmd, cwd=wd)


def clean(ctx):
    wd = 'doc'
    cmd = ['make', 'clean']
    ctx.exec_command(cmd, cwd=wd)


def test(ctx):
    t = ctx.path.ant_glob('src/**/*.py')
    files = [f.abspath() for f in t]
    ctx.exec_command('nosetests -vv ' + ' '.join(files))


def dist(ctx):
    #ctx.algo = 'zip' 
    ctx.excl  = ' **/.waf-1* **/*~ **/*.pyc **/*.swp **/.lock-w*' 
    ctx.files = ctx.path.ant_glob(['src/*', 'doc/*']) 

# vim: set et ts=4 sw=4 cindent fileencoding=utf-8 :

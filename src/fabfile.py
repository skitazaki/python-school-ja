from fabric.api import local, run, put

def hello():
    run("uname -s")

def check():
    local("pyflakes *.py")

def test():
    local("nosetests csv-*.py")

def deploy():
    put("downloader.py", "/tmp/downloader.py")

def all():
    check()
    test()
    deploy()

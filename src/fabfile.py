from fabric.api import local, run, put

def hello():
    run("uname -s")

def check():
    local("flake8 *.py")

def test():
    local("nosetests *.py")

def deploy():
    put("downloader.py", "/tmp/downloader.py")

def all():
    check()
    test()
    deploy()

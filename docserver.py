#!/usr/bin/env python
from livereload import Server, shell
server = Server()
server.watch('docs/*.txt', shell('make html', cwd='docs'))
server.serve(root='docs/_build/html')

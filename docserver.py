#!/usr/bin/env python
from livereload import Server, shell
server = Server()
server.watch('doc/*.txt', shell('make html', cwd='doc'))
server.serve(root='doc/_build/html')

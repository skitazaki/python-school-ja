#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import paramiko

server = "localhost"
username = password = None
try:
    u = getpass.getuser()
    username = input("Username: (Default=%s) " % (u,))
    if not username:
        username = u
    password = getpass.getpass("Password: ")
except KeyboardInterrupt:
    raise SystemExit("Cancel")

if not password:
    raise SystemExit("No password is given.")

t = paramiko.Transport((server, 22))
try:
    t.connect(username=username, password=password, hostkey=None)
except:
    t.close()
    raise SystemExit("Bad username or password.")

ch = t.open_channel(kind="session")
ch.exec_command("uptime")
if ch.recv_ready:
    print(server + ": " + ch.recv(1000))
t.close()

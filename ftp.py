#!/usr/bin/python3

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

PORT = 21
PASSIVE_PORTS = range(64000, 64001)
MAX_CONS = 10
MAX_CONS_PER_IP = 5
USERS = [
	['USERNAME', 'PASSWORD', 'PATH']
]

def start():
	authorizer = DummyAuthorizer()

	for user in USERS:
		authorizer.add_user(user[0], user[1], user[2], perm='elradfmw')
	handler = FTPHandler
	handler.authorizer = authorizer
	handler.banner = 'Welcome!'
	handler.passive_ports = PASSIVE_PORTS
	server = FTPServer(('', PORT), handler)
	server.max_cons = MAX_CONS
	server.max_cons_per_ip = MAX_CONS_PER_IP
	return server

start().serve_forever()

#!/usr/bin/python
from socket import *
from time import ctime
import sys
import select

# a simple echo server
# 1) accept only one client 
# 2) can exec shell cmd
class TcpSocketServer():
	def __init__(self):
		self.host = 'localhost'
		self.port = 21567
		self.buffsize = 1024
		self.addr = (self.host, self.port)

		self.s_socket = socket(AF_INET, SOCK_STREAM)
		self.s_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		self.s_socket.bind(self.addr)
		self.s_socket.listen(5)
		self.inputs = [self.s_socket,sys.stdin]

	def run(self):
		try:
			while True:
				print 'Waiting for connection...'
				self.c_socket, c_addr = self.s_socket.accept()
				print 'Connection from c_addr',c_addr
				self.inputs.append(self.c_socket)

				while True:
					inputs,outputs,exceptions = select.select(self.inputs, [], [])
					for io in inputs:
						if io == self.c_socket:
							data = self.c_socket.recv(self.buffsize)
							if not data:
								break
							print c_addr,':',data
						# sys.stdin
						else:
							#  diff from 2-5
							send = raw_input('')
							if not send:
								break
							self.c_socket.send('[%s] %s' % (ctime(), send))
				self.c_socket.close()
				self.inputs.remove(self.c_socket)
				self.c_socket = None
		except KeyboardInterrupt, e:
			print 'CTRL+C end the server'
			self.s_socket.close()

tcp = TcpSocketServer()
tcp.run()

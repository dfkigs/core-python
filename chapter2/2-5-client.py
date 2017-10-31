#!/usr/bin/python
from socket import *
from time import ctime

class TcpSocketClient():
	def __init__(self):
		self.host = 'localhost'
		self.port = 21567
		self.buffsize = 1024
		self.addr = (self.host, self.port)
		
		self.c_socket = socket(AF_INET, SOCK_STREAM)

	def run(self):
		try:
			self.c_socket.connect(self.addr)
		
			while True:
				data = raw_input("> ")
				if not data:
					break
			
				self.c_socket.send(data)
				recv = self.c_socket.recv(self.buffsize)
				if not recv:
					break
				print recv
			self.c_socket.close()
		except :
			print 'CTRL+C end the client'
			self.c_socket.send('Bye...')
			self.c_socket.close()

c_tcp = TcpSocketClient()
c_tcp.run()

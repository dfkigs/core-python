#!/usr/bin/python
from socket import *
from time import ctime

class UDPSocketServer():
	def __init__(self):
		self.host = 'localhost'
		self.port = 21567
		self.buffsize = 1024
		self.addr = (self.host, self.port)
	
		self.s_udp_socket = socket(AF_INET, SOCK_DGRAM)
		self.s_udp_socket.bind(self.addr)

		self.daytime_port = getservbyname('daytime','udp')
		print 'self.daytime_port = ', self.daytime_port

	def run(self):
		try:
			while True:
				print 'Waiting for data...'
				data, addr = self.s_udp_socket.recvfrom(self.buffsize)
				if not data:
					break
				print 'Received from addr',addr,data
				self.s_udp_socket.sendto('[%s] %s' % (ctime(), data), addr)
			self.s_udp_socket.close()
		except KeyboardInterrupt, e:
			print 'CTRL+C end the server'
			self.s_udp_socket.close()

udp_socket = UDPSocketServer()
udp_socket.run()

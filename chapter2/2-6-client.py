#!/usr/bin/python
from socket import *

class UDPSocketClient():
	def __init__(self):
		self.host = 'localhost'
		self.port = 21567
		self.buffsize = 1024
		self.addr = (self.host, self.port)
		
		self.c_udp_socket = socket(AF_INET, SOCK_DGRAM)
		
	def run(self):
		try:
			while True:
				send = raw_input('>')
				if not send:
					break
				self.c_udp_socket.sendto(send, self.addr)
				recv, addr = self.c_udp_socket.recvfrom(self.buffsize)
				if not recv:
					break
				print recv
			self.c_udp_socket.close()
		except KeyboardInterrupt, e:
			print 'CTRL+C end the client'
			self.c_udp_socket.close()

c_udp_socket = UDPSocketClient()
c_udp_socket.run()

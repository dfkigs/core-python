#!/usr/bin/python
from socket import *
from time import ctime
import os 
import commands
import re

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

	def run(self):
		try:
			while True:
				print 'Waiting for connection...'
				c_socket, c_addr = self.s_socket.accept()
				print 'Connection from c_addr',c_addr
				while True:
					data = c_socket.recv(self.buffsize)
					if not data:
						break
					print c_addr,':',data
					m = re.search('(?<=exec).*', data)
					if m:
						c_socket.send('[%s] [%s]' % (ctime(), self.exec_cmd(m.group())))
					else:
						c_socket.send('[%s] [%s] [%s] %s' % (ctime(), os.name, os.listdir(os.curdir), data))
				c_socket.close()
		except KeyboardInterrupt, e:
			print 'CTRL+C end the server'
			self.s_socket.close()

	def exec_cmd(self, args):
		#os.system(args)
		(status, output) = commands.getstatusoutput(args)
		#output = commands.getoutput(args)
		#status = commands.getstatus(args)
		return output
		
tcp = TcpSocketServer()
tcp.run()

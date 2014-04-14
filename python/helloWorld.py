#coding=utf-8
import os
import socket

def helloWorld(name):
	print "Hello World,",name

def helloWorldWithInput():
	content = raw_input("please input your name:\n")
	print "Hello World,",content

def helloWorldWithFile():
	filepath = raw_input("please input filename:\n")
	file = open(filepath,'r')
	print "Hello World,",file.readline()

def helloWorldWithNetWork():
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.bind(('localhost',8001))
	sock.listen(5)
	while True:
		connection,address = sock.accept()
		try:
			connection.settimeout(5)
			buf = connection.recv(1024)
			print buf
			if buf == 'welcome':
				connection.send("welcome to server")
			elif buf == 'quit':
				connection.close()
			else:
				connection.send('please go out')
			
		except socket.timeout:
			print 'time out'
		

if __name__ == '__main__':
	helloWorld('jotZhao')
	helloWorldWithInput()
	helloWorldWithFile()
	helloWorldWithNetWork()

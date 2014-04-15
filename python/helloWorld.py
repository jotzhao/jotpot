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
	sock.bind(('localhost',9001))
	sock.listen(5)
	while True:
		print 'waiting for connection'
		connection,address = sock.accept()
		print 'connection from :',address
		adminCommand=''
		while True:
			command = ''
			while True:
				buf = connection.recv(1024)
				if (len(buf)>1 and buf[1]=='\n'):
					break
				command =  command + buf
			print command 
			if command == 'welcome':
				connection.send("welcome to server\n")
			elif command == 'quit':
				connection.close()
				break
			elif command == 'shutdown':
				adminCommand=command
				connection.close()
				break
			else:
				connection.send('please go out\n')
		if adminCommand=='shutdown':
			break
	sock.close()
if __name__ == '__main__':
	#helloWorld('jotZhao')
	#helloWorldWithInput()
	#helloWorldWithFile()
	helloWorldWithNetWork()

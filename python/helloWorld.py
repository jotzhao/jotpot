#coding=utf-8
import os

def helloWorld(name):
	print "Hello World,",name

def helloWorldWithInput():
	content = raw_input("please input your name:\n")
	print "Hello World,",content

def helloWorldWithFile():
	filepath = raw_input("please input filename:\n")
	file = open(filepath,'r')
	print "Hello World,",file.readline()

if __name__ == '__main__':
	helloWorld('jotZhao')
	helloWorldWithInput()
	helloWorldWithFile()

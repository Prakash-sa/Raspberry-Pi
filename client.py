import socket

HOST = '' # Enter IP or Hostname of your server
PORT = 12345 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#Lets loop awaiting for your input
while True:
	command = raw_input('Enter your command: ')
	s.send(command)
	reply = s.recv(1024)
		if reply == 'Terminate':
			break
		print reply
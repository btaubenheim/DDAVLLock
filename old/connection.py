def socketconnect(socketname,ip,port):
	socketname=socket.create_connection(str(ip), port)
	return socketname

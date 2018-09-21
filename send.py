import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(str.encode('sup'), ("127.0.0.1", 5002 ))


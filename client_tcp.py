import socket

sock = socket.socket(socket.AF_INET, socket.INADDR_ANY)

sock.connect(("127.0.0.1", 1231))
sock.send(bytes("hi from client", encoding="utf-8"))
data = sock.recv(4096)
print(str(data, encoding="utf-8"))

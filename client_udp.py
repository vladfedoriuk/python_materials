import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
buffer = 4096
serv_info = ("127.0.0.1", 4451)
client.sendto(bytes("hello from client", encoding="utf-8"), serv_info)
message, address = client.recvfrom(buffer)

print("Message: {}".format(str(message, encoding="utf-8")))
print("Address: {}".format(str(address)))

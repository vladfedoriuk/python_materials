import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv.bind(("127.0.0.1", 4451))

buffer = 4096
while True:
    message, address = serv.recvfrom(buffer)
    print("Message from client: {}".format(str(message, encoding="utf-8")))
    print("Client IP address: {}".format(str(address)))
    if not message:
        break
    serv.sendto(bytes("received\n", encoding="utf-8"), address)

import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serv_info = ("127.0.0.1", 2020)
serv.setblocking(False)
serv.settimeout(5.0)
buffer = 4096
try:
    while True:
        s = input()
        if s == "quit":
            break
        serv.sendto(bytes(s, encoding="utf=8"), serv_info)
        try:
            message, address = serv.recvfrom(buffer)
        except socket.timeout:
            print("oops, time is out")
        else:
            print(str(message, encoding="utf-8"))
finally:
    serv.close()

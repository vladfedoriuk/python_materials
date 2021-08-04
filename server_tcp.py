import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("127.0.0.1", 1231))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ""
    while True:
        data = conn.recv(4096)
        if not data:
            break
        from_client += str(data, encoding="utf-8")
        form = "info: {0}, address: {1}\n"
        print(form.format(from_client, addr))
        ans = "received\n"
        conn.send(bytes(ans, encoding="utf-8"))
    conn.close()

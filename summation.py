import socket


class UDP:
    def __enter__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serv.bind(("127.0.0.1", 2020))
        return self.serv

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.serv.close()
        return exc_type is None


class Form(object):
    def __init__(self, data, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.data = str(data, encoding="utf-8")

    def validate(self):
        if "\t" in self.data:
            return False
        try:
            self.__setattr__("nums", list(map(int, self.data.split())))
        except ValueError or TypeError:
            return False
        if len(list(filter(lambda x: x >= 0, getattr(self, "nums")))) != len(
            getattr(self, "nums")
        ):
            return False
        return True

    def sum(self):
        return sum(getattr(self, "nums"))


buffer = 4096

with UDP() as serv:
    while True:
        data, address = serv.recvfrom(buffer)
        if data == b"\r\n" or data == b"\n" or not data:
            serv.sendto(bytes("ERROR", encoding="utf-8"), address)
        else:
            form = Form(data)
            if not form.validate():
                serv.sendto(bytes("ERROR", encoding="utf-8"), address)
            else:
                serv.sendto(bytes(str(form.sum()), encoding="utf-8"), address)

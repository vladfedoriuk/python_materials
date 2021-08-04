import socket
import sys
import unittest


class ServerTest(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serv_info = ("127.0.0.1", 2020)
        self.sock.setblocking(False)
        self.sock.settimeout(3)

    def fun(self, nums):
        buffer = 4096
        self.sock.sendto(bytes(nums, encoding="utf-8"), self.serv_info)
        try:
            out, address = self.sock.recvfrom(buffer)
        except socket.timeout:
            return None
        return str(out, encoding="utf-8").strip()

    def compare_files(self, tests_file, tests_res):
        with open(tests_file, "r") as tests:
            with open(tests_res, "r") as results:
                for nums, summ in zip(tests, results):
                    test = self.fun(nums)
                    self.assertEqual(test, summ.strip())


t = ServerTest()
t.compare_files(str(sys.argv[1]), str(sys.argv[2]))

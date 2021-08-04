file = open("in.txt", "r")
try:
    line = file.readline()
    print(line)
finally:
    file.close()


def controlled_execution(fun):
    file = open("in.txt", "a")
    try:
        res = fun(file)
    finally:
        file.close()
    return res


def fun(file):
    file.write("\ndecorator")


controlled_execution(fun)


def controlled_execution():
    file = open("in.txt", "r")
    try:
        yield file
    finally:
        file.close()


lines = []
for f in controlled_execution():
    lines = f.readlines()

print(lines)

lines = [x.strip() for x in lines if len(x) > 1]
print(lines)


class ControlledExecution:
    def __enter__(self):
        self.f = open("in.txt", "w")
        return self.f

    def __exit__(self, exception_type, exception_value, traceback):
        self.f.close()
        return True


with ControlledExecution() as f:
    for x in list(set(lines)):
        f.write(x + "\n")


with open("in.txt", "r") as f:
    print(f.readlines())

def f(x, a):
    return 4 * a * x * (1 - x)


a = 0.875
x = 0.3
# x=0.1


def multicycle(f, x, *args):
    res = str(x)
    s = ""
    while True:
        x = f(x, *args)
        x_str = " %.2f" % x
        res = res + x_str
        for i in range(len(res) - 1, 0, -1):
            other = res[:i]
            cycle = res[i:]
            if (
                other.find(cycle) != -1
                and len(cycle.split(" ")) == len(set(cycle.split(" ")))
                and cycle[0] == " "
            ):
                if len(cycle) > len(s):
                    s = cycle
        print("res= ", res)
        yield s


[print("cycle= ", y) for y, r in zip(multicycle(f, x, a), range(100))]

t = [
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]

d = []


def find_path(x, y):
    global d, t
    if x >= len(t) or y >= len(t[x]) or x < 0 or y < 0:
        return False
    if t[x][y] != 0:
        return False
    if x == 0 or y == 0 or x == len(t) - 1 or y == len(t[x]) - 1:
        return True
    d.append((x, y))
    t[x][y] = "x"
    if find_path(x + 1, y):
        return True
    if find_path(x, y + 1):
        return True
    if find_path(x - 1, y):
        return True
    if find_path(x, y - 1):
        return True
    d.pop()
    t[x][y] = 0
    return False


if find_path(5, 1):
    print(d)

print(sum([str(x).count("8") for x in range(1, 100)]))

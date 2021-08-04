import json


def read(filename):
    with open(filename) as f:
        return f.read()


def write(
    filename,
    info,
    mode="w",
):
    with open(filename, mode=mode) as f:
        f.write(info)


if __name__ == "__main__":
    data = read("data.json")
    print("raw data is", data, type(data))

    # from string to object  (dict)
    obj = json.loads(data)
    print(obj, type(obj))

    print(obj["boolean"])
    print(obj["string"])

    # from object to text
    print("dumping object to text")
    obj["new-value"] = "secret"
    txt = json.dumps(obj, sort_keys=True, indent=4)
    print(txt)

    obj = json.load(open("data.json"))
    print(obj)
    obj["example"] = -1
    s = json.dump(obj, open("data1.json", mode="w"), indent=4, sort_keys=True)
    print(s)

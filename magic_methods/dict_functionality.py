class DictFunctionality(object):
    def __init__(self, values=None):
        if values is None:
            self.values = {}
        elif isinstance(values, dict):
            self.values = values
        else:
            raise ValueError()

    # Converting to string:
    def __str__(self):
        return str(self.values) if self.values else ""

    # Items management:
    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    # Iteration:
    def __iter__(self):
        return iter(self.values)

    # `in` operation:
    def __contains__(self, item):
        return item in self.values

    def __len__(self):
        return len(self.values)  # self.values.__len__()


if __name__ == "__main__":
    l = DictFunctionality({"1key": "some_value"})
    l[1] = "item1"
    print(str(l), l[1])

    for item in l:
        print(item, l[item])

    print("s" in l, 1 in l)
    print(len(l))

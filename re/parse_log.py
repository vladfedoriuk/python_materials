import re


def read_and_parse(filename):
    with open(filename) as f:
        for line in f:
            # yield (parse_date(line), parse_place(line))
            match = parse_log(line)
            if match:
                yield match.groups()


def parse_date(txt):
    pattern = r"(\d\d\/\w+\/\d{4})"
    return re.findall(pattern, txt)


def parse_place(txt):
    pattern = r"([a-zA-Z.]+:\d+)"
    return re.findall(pattern, txt)


def parse_log(txt):
    p = re.compile(r"^.(\d{2}.\w+.\d{4}).*?\] DEBUG .([\w\.]+:\d+). (.*$)")
    return p.search(txt)


if __name__ == "__main__":
    [print(x) for x in read_and_parse("ParseData.txt")]

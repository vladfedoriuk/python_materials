try:
    import urllib.request
    import urllib.parse
    import urllib.error
except ImportError as e:
    print(e)


def write(s, name="out.html", mode="w"):
    with open(name, mode=mode) as f:
        f.write(s)


def get_habrahabr():
    try:
        response = urllib.request.urlopen("http://habrahabr.ru/")
        print(response.code)
        print(response.info())
        print(response.geturl())
        html = response.read()
        response.close()
        print(html)
    except urllib.error.HTTPError as e:
        print(e)
    except urllib.error.URLError as e:
        print(e)


def parse_url():
    try:
        parse_ur = urllib.parse.urlparse(
            "https://www.geeksforgeeks.org/python-urllib-module/"
        )
        print(parse_ur)
        unparse_url = urllib.parse.urlunparse(parse_ur)
        print(unparse_url)

        split_url = urllib.parse.urlsplit(
            "https://www.geeksforgeeks.org/python-urllib-module/"
        )
        print(split_url)
        unsplit_url = urllib.parse.urlunsplit(split_url)
        print(unsplit_url)
    except urllib.error.URLError as e:
        print(e.reason)


def get_python():
    with urllib.request.urlopen("http://python.org") as response:
        html = response.read()
        return html


def get_python1():
    req = urllib.request.Request("http://python.org")
    with urllib.request.urlopen(req) as response:
        print(response.code)
        print(response.geturl())
        print(response.info())
        html = response.read()
        return html


def post_request():
    # url = 'http://www.someserver.com/cgi-bin/register.cgi'
    url = "http://google.com"
    values = {"name": "Vlad", "age": 19, "language": "Python"}

    data = urllib.parse.urlencode(values)
    data = data.encode(encoding="utf-8")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.code)  # http code
        print(response.info())  # headers (meta data)
        print(response.geturl())  # actual url from which the data was fetched
        return str(response.read(), encoding="utf-8")  # data


def post_request1():
    data = {}
    data["name"] = "Vlad"
    data["age"] = 19
    data["language"] = "Python"
    url_values = urllib.parse.urlencode(data)
    print(url_values)
    url = "http://google.com"
    full_url = url + "?" + url_values
    with urllib.request.urlopen(full_url) as response:
        return str(response.read(), encoding="utf-8")


def post_request_with_headers():
    data = {"name": "Vlad", "age": 19, "language": "Python"}
    url = "http://python.org"
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    headers = {"User-Agent": user_agent}
    data = urllib.parse.urlencode(data)
    data = data.encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req) as response:
        return str(response.read(), encoding="utf-8")


def wrapping_up():
    url = "http://smth.org"
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as he:
        print("The server cannot fulfil a request")
        print("Error code", he.code)
    except urllib.error.URLError as ue:  # super class of HTTPError
        print("Cannot reach a server")
        print(ue.reason)
    except Exception as e:
        print("Exception occured", e)
    else:
        print("Everything is fine")
        print(response.read())


if __name__ == "__main__":
    # get_habrahabr()
    # parse_url()
    # print(get_python())
    # print(get_python1())
    try:
        print(post_request())
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.reason)
        print(e.read())

    try:
        write(post_request1())
    except urllib.error.HTTPError as e:
        print(e.code)

    try:
        write(post_request_with_headers())
    except urllib.error.HTTPError as e:
        print(e.code)

    wrapping_up()

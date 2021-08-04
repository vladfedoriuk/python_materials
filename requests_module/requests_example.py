import requests
import requests.auth
import json
import requests.exceptions
import requests.adapters


def getpass():
    return "20122000vl"


def get_habrahabr():
    r = requests.get("http://habrahabr.ru")
    print(r.status_code)
    print(r.headers)
    print(r.content)


def write(txt, filename="data.txt", mode="w"):
    with open(filename, mode=mode) as f:
        f.write(txt)


def get_example():
    response = requests.get("http://api.github.com")
    print(response)
    print("Status code:", response.status_code)

    if response:  # equivalent to (200 <= response.status_code < 400)
        print("Success")
    else:
        print("failure")

    print(response.content)  # raw data bytes
    response.encoding = "utf-8"  # optional, it will be deducted using returned headers
    print(response.text)  # raw bytes converted into utf-8 string
    obj = response.json()  # equivalent to json.loads(response.text)
    print(obj)

    headers = response.headers  # HTTP headers
    print(headers)
    print(headers["Content-Type"])
    print(headers["content-type"])  # the same as before


def customize_get():
    response = requests.get(
        url="http://api.github.com/search/repositories",
        params={"q": "requests+language:python"},
        headers={
            "Accept": "application/vnd.github.v3.text-match+json",
        },
    )
    write(json.dumps(response.text, indent=4, sort_keys=True))
    json_response = response.json()
    repo = json_response["items"][0]
    print(f'Repository name: {repo["name"]}')
    print(f'Repository description: {repo["description"]}')


def other_verbs():
    response = requests.post(url="http://httpbin.org/post", json={"vlad": 19})

    print("POST response", response.text)
    print(response.json())

    print("Request url", response.request.url)
    print("Request headers", response.request.headers)
    print("Request body", response.request.body)

    response = requests.put(url="http://httpbin.org/put", data={"args": 19})
    print("PUT response", response.text),

    response = requests.get(
        url="http://httpbin.org/get",
        params={"args": 19},
        headers={"Accept": "application/json"},
    )
    print("ARGS", response.json()["args"])

    print("CONTENT-TYPE header", response.headers["content-type"])
    print("GET response", response.text)

    response = requests.delete("https://httpbin.org/delete")
    print("DELETE response", response.text)

    response = requests.head("https://httpbin.org/get")
    print("HEAD response", response.text)

    response = requests.patch("https://httpbin.org/patch", data={"args": 19})
    print("PATCH response", response.text)

    response = requests.options("https://httpbin.org/get")
    print("OPTIONS response", response.text)


def authentication_example():
    try:
        response = requests.get(
            "http://api.github.com/user", auth=("vladfedoriuk", getpass()), timeout=5
        )
    except requests.exceptions.Timeout as te:
        print(f"Timeout exception: {e}")

    # print(response.json())
    res = response.json()
    response = requests.post(
        url="https://api.github.com/user",
        data=json.dumps(
            {
                "name": res["name"],
                "email": res["email"],
                "blog": res["blog"],
                "company": res["company"],
                "location": "Chernivtsi",
                "hireable": True,
                "bio": "computer science student",
            }
        ),
        auth=requests.auth.HTTPBasicAuth(
            "vladfedoriuk", getpass()
        ),  # the same as above
    )
    print(response.json())
    print(response.status_code)


def exception_example():
    for url in ["http://api.github.com", "http://api.github.com/invalid"]:
        try:
            response = requests.get(url)
            response.raise_for_status()  # if the response was successful, no exception will be thrown
        except requests.HTTPError as e:
            print(f"HTTP error: {e}")
        except Exception as ex:
            print(f"Exception: {ex}")


def session_object():
    # By using a context manager, you can ensure the resources used by
    # the session will be released after use
    with requests.Session() as session:
        session.auth = ("vladfedoriuk", getpass())
        # Instead of requests.get(), you'll use session.get()
        response = session.get("https://api.github.com/users/vladfedoriuk/repos").json()
        print("repos:")
        for repo in response:
            print(f'id: {repo["id"]}, name: {repo["name"]}')


def transport_adapter():
    github_adapter = requests.adapters.HTTPAdapter(max_retries=3)
    with requests.Session() as session:
        session.mount("https://api.github.com", github_adapter)
        try:
            response = requests.get("https://api.github.com", timeout=5)
            print(response.text)
        except ConnectionError as ce:
            print(ce)
        except requests.exceptions.Timeout as te:
            print(te)


def find_pet_by_tag(tag):
    params = {"tags": tag}
    headers = {
        # 'Accept': 'application/xml'
        "Accept": "application/json"
    }
    url = "http://petstore.swagger.io/v2/pet/findByTags"
    req = requests.get(url=url, params=params, headers=headers)
    print(req.status_code, req.headers)
    s = str(req.content, encoding="utf-8")
    obj = json.loads(s)
    write(json.dumps(obj, indent=4, sort_keys=True))


if __name__ == "__main__":
    # get_habrahabr()
    # find_pet_by_tag('string')
    # get_example()
    # exception_example()
    try:
        # customize_get()
        # other_verbs()
        # authentication_example()
        # session_object()
        transport_adapter()
        print()
    except requests.HTTPError as e:
        print(e)
    except Exception as ex:
        print("exception occurred", ex)

    response = requests.get(
        "https://httpbin.org/image", headers={"accept": "image/png"}
    )
    write(response.content, "image.png", mode="wb")

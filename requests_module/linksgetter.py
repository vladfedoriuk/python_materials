import requests
import re


def get_links(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    response = requests.get(
        url=url,
        headers={"user-agent": user_agent},
    )
    response.raise_for_status()
    response = response.text
    p = re.compile(r"(https?://[\d\w/.\-_]+)")
    for x in p.finditer(response):
        yield x.group()


if __name__ == "__main__":
    try:
        for x in get_links(
            "https://stackoverflow.com/questions/2150192/how-to-avoid-code-duplication-implementing-const-and-non-const-iterators"
        ):
            print(x)
    except requests.HTTPError as he:
        print(f"Http error: {he}")
    except Exception as e:
        print(f"Exception: {e}")

import requests


def print_user_comment(url):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
    response = requests.get(
        url=url,
        headers={
            "Accept": "application/json",
            "user-agent": user_agent,
        },
    )
    response.raise_for_status()
    response = response.json()
    for i in range(0, 7):
        print("Author: ", response[1]["data"]["children"][i]["data"]["author"])
        print("Comment: ", response[1]["data"]["children"][i]["data"]["body"])


if __name__ == "__main__":
    try:
        print_user_comment(
            "https://www.reddit.com/r/Python/comments/g9nvzi/whats_everyone_working_on_this_week/.json"
        )
    except requests.HTTPError as he:
        print(he)
    except Exception as e:
        print(e)

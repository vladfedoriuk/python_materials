import requests.auth


class MyAuthentication(requests.auth.AuthBase):
    def __init__(self, token, *args, **kwargs):
        self.token = token
        super().__init__(*args, **kwargs)

    def __call__(self, request):
        """' Attach an API token to a custom auth header"""
        request.headers["X-TokenAuth"] = f"{self.token}"
        return request

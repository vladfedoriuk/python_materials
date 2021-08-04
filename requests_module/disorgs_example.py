import requests
import requests.exceptions
import requests.adapters
from collections import defaultdict
import functools
import logging
import sys


class NotABandError(Exception):
    pass


"""Setting logger parameters"""
logger = logging.getLogger(__name__)
f_handler = logging.FileHandler("disorgs.log", mode="w")
c_handler = logging.StreamHandler()
f_handler.setLevel(logging.ERROR)
c_handler.setLevel(logging.INFO)
f_formatter = logging.Formatter(
    "%(asctime)s - %(name)s -  %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S"
)
c_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_handler.setFormatter(f_formatter)
c_handler.setFormatter(c_formatter)
logger.addHandler(f_handler)
logger.addHandler(c_handler)


class Artist(object):
    def __init__(self, artist_id, *args, **kwargs):
        super(Artist, self).__init__(*args, **kwargs)
        self.artist_id = artist_id

        with requests.session() as session:
            self.logger = logging.getLogger(__name__)
            try:
                discogs_adapter = requests.adapters.HTTPAdapter(max_retries=3)
                session.mount(
                    f"https://api.discogs.com/artists/{artist_id}", discogs_adapter
                )

                response = session.get(
                    url=f"https://api.discogs.com/artists/{artist_id}",
                    headers={
                        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)",
                        "accept": "application/json",
                    },
                    timeout=5,
                )
                response.raise_for_status()
                self.data = response.json()

            except requests.HTTPError as he:
                self.logger.exception(
                    msg="HTTP ERROR in Artist.__init__", exc_info=True
                )
            except requests.exceptions.Timeout as te:
                self.logger.exception(
                    msg="TIMEOUT ERROR in Artist.__init__", exc_info=True
                )
            except Exception as e:
                self.logger.exception(msg="EXCEPTION in Artist.__init__", exc_info=True)

    def __getitem__(self, item):
        return self.data.get(item)

    name = functools.partialmethod(__getitem__, "name")
    uri = functools.partialmethod(__getitem__, "uri")


class Band(Artist):
    def __init__(self, band_id, *args, **kwargs):
        super(Band, self).__init__(band_id, *args, **kwargs)
        if "members" not in self.data:
            raise NotABandError("artist is not a band")

    @property
    def participants(self):
        it = iter(self.data["members"])
        while True:
            try:
                el = next(it)
            except StopIteration:
                break
            else:
                yield el["id"], el["name"]


if __name__ == "__main__":
    band_id = sys.argv[1]
    b = Band(band_id)
    print(b.name(), b.uri())
    data = defaultdict(list)
    for member_id, member_name in b.participants:
        member = Artist(member_id)
        if member:
            groups = member["groups"]
            for group in groups:
                data[group["name"]].append(member["name"])

    data.pop(b.name())
    data = {k: v for k, v in data.items() if len(v) > 1}
    for k, v in sorted(data.items(), key=lambda x: -len(x[1])):
        print(f"Band name: {k}\n\tMembers: {v}")

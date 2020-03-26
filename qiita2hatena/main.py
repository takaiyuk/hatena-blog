import base64
from datetime import datetime
import hashlib
import os
import requests
import random
from typing import Tuple
import warnings
from xml.sax.saxutils import escape
import yaml


def load_yaml(path: str = "config.yml") -> dict:
    with open(path, "r") as f:
        return yaml.load(f)


class Qiita:
    def __init__(self, config: str) -> None:
        self.user = config["QIITA_USER"]
        self.output_dir = config["OUTPUT_DIR"]

    def _mkdir(self, path: str) -> None:
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    def prepare(self) -> None:
        self._mkdir(self.output_dir)

    def get(self) -> None:
        return requests.get(
            f"https://qiita.com//api/v2/users/{self.user}/items?per_page=100"
        )

    def parse(self, content: str) -> Tuple[str, str, str, str]:
        body = content["rendered_body"]
        created_at = content["created_at"]
        title = content["title"]
        updated_at = content["updated_at"]
        url = content["url"]
        return (body, created_at, title, updated_at, url)

    def write(self, body: str, title: str) -> None:
        self._mkdir(f"{self.output_dir}/{title}")
        with open(f"{self.output_dir}/{title}/index.md", "w") as f:
            f.write(body)

    def save(self) -> None:
        self.prepare()
        r = self.get()
        for content in r.json():
            body, created_at, title, updated_at, url = self.parse(content)
            joined_body = "\n\n".join([url, created_at, updated_at, body])
            self.write(joined_body, title)


class Hatena:
    """ref.) https://qiita.com/virtual_techX/items/5179b73576d86a89868e"""

    def __init__(self, config: str) -> None:
        self.output_dir = config["OUTPUT_DIR"]
        self.user = config["HATENA_USER"]
        self.blog = config["HATENA_BLOG"]
        self.apikey = config["HATENA_APIKEY"]

    def create_hatena_text(
        self, title: str, body: str, categories: list, is_draft: bool
    ):
        updated = datetime.now()
        is_draft = "yes" if is_draft else "no"
        categories_text = ""
        if categories:
            for category in categories:
                categories_text = categories_text + f'<category term="{category}" />\n'

        template = """<?xml version="1.0" encoding="utf-8"?>
        <entry xmlns="http://www.w3.org/2005/Atom"
            xmlns:app="http://www.w3.org/2007/app">
        <title>{0}</title>
        <author><name>{1}</name></author>
        <content type="text/x-markdown">{2}</content>
        <updated>{3}</updated>
        {4}
        <app:control>
            <app:draft>{5}</app:draft>
        </app:control>
        </entry>"""
        text = template.format(
            title, self.user, body, updated, categories_text, is_draft
        ).encode()
        return text

    def create_wsse_auth_text(self):
        created = datetime.now().isoformat() + "Z"
        b_nonce = hashlib.sha1(str(random.random()).encode()).digest()
        b_digest = hashlib.sha1(
            b_nonce + created.encode() + self.apikey.encode()
        ).digest()
        c = 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'
        return c.format(
            self.user,
            base64.b64encode(b_digest).decode(),
            base64.b64encode(b_nonce).decode(),
            created,
        )

    def post(self):
        url = f"https://blog.hatena.ne.jp/{self.user}/{self.blog}/atom/entry"

        dirs = os.listdir(f"./{self.output_dir}")
        for title in dirs:
            if title == ".DS_Store":
                continue
            with open(f"./{self.output_dir}/{title}/index.md", "r") as f:
                body = escape(f.read())
            data = self.create_hatena_text(title, body, categories=[], is_draft=True)
            headers = {
                "X-WSSE": self.create_wsse_auth_text(),
                "content-type": "application/xml",
            }
            request = requests.post(url, data=data, headers=headers)
            if request.status_code == 201:
                print(f"POST SUCCESS: {title}")
            else:
                print(
                    f"Error!\nstatus_code: {str(request.status_code)}\nmessage: {request.text}"
                )


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    config = load_yaml()
    Qiita(config).save()
    Hatena(config).post()

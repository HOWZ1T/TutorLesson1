import requests
from bs4 import BeautifulSoup

__wiki_base_url__ = "https://en.wikipedia.org/wiki/"


def download_picture(url: str, dest: str) -> None:
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception(f"get request failed with status_code: {resp.status_code}")

    with open(dest, "wb") as f:
        for block in resp.iter_content(1024):
            if not block:
                break

            f.write(block)

        print(f"saved file: {dest}")


def get_wiki_picture(wiki: str, download: bool = False) -> str:
    url = f"{__wiki_base_url__}{wiki}"
    print(f"requesting content from: {url}")

    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception(f"get request failed with status_code: {resp.status_code}")

    soup = BeautifulSoup(resp.content, 'html.parser')
    img = soup.select_one(".image").find("img")["src"]
    img = "https:" + img

    if download:
        download_picture(img, f"pictures/{img.split('/')[-1].split('-')[-1]}")

    return img


if __name__ == "__main__":
    print(get_wiki_picture("kim_kardashian", True))

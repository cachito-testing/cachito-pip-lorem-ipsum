import requests


def main():
    r = requests.get("https://loripsum.net/api/plaintext")
    print(r.text)

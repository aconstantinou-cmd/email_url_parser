#!/usr/bin/env python3


import argparse
import re
import requests
from bs4 import BeautifulSoup


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Enter a URL")
    args = parser.parse_args()
    return args


def get_html(url):
    response = requests.get(url,allow_redirects=False)
    return response.text


def find_emails(html):
    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
    return emails


def main():
    args = get_arguments()
    url = args.url
    html = get_html(url)
    emails = find_emails(html)
    print("Emails:")
    for email in emails:
        print(email)


if __name__ == "__main__":
    main()
    
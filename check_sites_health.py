import os
import requests
import whois
from datetime import datetime


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as handler:
        content = handler.readlines()
        return [url.rstrip('\n') for url in content]


def is_server_respond_with_200(url):
    try:
        request = requests.get(url)
        return True if request.status_code == 200 else False
    except requests.exceptions.ConnectionError:
        return False


def get_domain_expiration_date(domain_name):
    try:
        domain_info = whois.query(domain_name)
        return domain_info.expiration_date
    except AttributeError:
        return None


if __name__ == '__main__':
    urls = load_urls4check('urls.txt')
    domains = [domain.lstrip('http://') for domain in urls]
    for url in urls:
        if is_server_respond_with_200(url):
            print('{} - OK!'.format(url))
        else:
            print('{} - ERROR!'.format(url))
    for domain in domains:
        if get_domain_expiration_date(domain)




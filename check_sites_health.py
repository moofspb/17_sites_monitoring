import os
import argparse
import requests
import whois
from datetime import datetime, timedelta


DAYS_LIMIT = timedelta(days=30)


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
        return None


def get_domain_expiration_date(domain):
    try:
        domain_info = whois.query(domain)
        return domain_info.expiration_date
    except AttributeError:
        return None


def check_need_to_pay_domain(domain, days_limit):
    try:
        if get_domain_expiration_date(domain) - datetime.now() > days_limit:
            return True
        else:
            return False
    except TypeError:
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check status of sites from txt file. Status / '
                                                 'is OK if response status HTTP 200 and there / '
                                                 'is more than month till expiration date.')
    parser.add_argument('filepath', help='A path to a text file')
    args = parser.parse_args()
    urls = load_urls4check(args.filepath)
    for url in urls:
        if is_server_respond_with_200(url) and \
                check_need_to_pay_domain(url.lstrip('http://'), DAYS_LIMIT):
            print('{} - OK!'.format(url))
        if check_need_to_pay_domain(url.lstrip('http://'), DAYS_LIMIT) is None:
            print('{} - Can\'t get an expiration date!'.format(url))
        elif not check_need_to_pay_domain(url.lstrip('http://'), DAYS_LIMIT):
            print('{} - It\'s time to pay domain!'.format(url))
        if not is_server_respond_with_200(url):
            print('{} - No connection!'.format(url))

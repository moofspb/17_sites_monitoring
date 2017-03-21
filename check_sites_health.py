import os
import argparse
import requests
import whois
from datetime import datetime, timedelta


def get_script_args():
    parser = argparse.ArgumentParser(
        description='Check status of sites from txt file. Status / '
                    'is OK if response status HTTP 200 and there / '
                    'is more than month till expiration date.')
    parser.add_argument('filepath', help='A path to a text file')
    args = parser.parse_args()
    return args.filepath


def load_urls4check(path):
    if not os.path.exists(path):
        return None
    with open(path, 'r') as handler:
        content = handler.readlines()
        return [url.rstrip('\n') for url in content]


def is_server_respond_with_200(url):
    try:
        request = requests.get(url)
        return request.status_code == 200
    except requests.exceptions.ConnectionError:
        return None


def get_domain_expiration_date(domain):
    try:
        domain_info = whois.query(domain)
        return domain_info.expiration_date
    except AttributeError:
        return None
    except ValueError:
        return None


def check_need_to_pay_domain(domain, days_limit=30):
    try:
        return get_domain_expiration_date(domain) - datetime.now() < timedelta(days_limit)
    except TypeError:
        return None


def print_sites_status(url, is_status_200, is_time_to_pay_domain):
    if is_status_200:
        print('{} -HTTP status is OK! (200)'.format(url))
    else:
        print('{} - No connection!'.format(url))
    if not is_time_to_pay_domain:
        print('{} - Domain paid!'.format(url))
    elif is_time_to_pay_domain is None:
        print('{} - Can\'t get an expiration date!'.format(url))
    else:
        print('{} - It\'s time to pay domain!'.format(url))


if __name__ == '__main__':
    filepath = get_script_args()
    sites_urls = load_urls4check(filepath)
    for url in sites_urls:
        is_200 = is_server_respond_with_200(url)
        is_time_to_pay_domain = check_need_to_pay_domain(url.lstrip('http://'))
        print_sites_status(url, is_200, is_time_to_pay_domain)


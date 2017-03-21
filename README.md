# Sites Monitoring Utility

Check status of sites from txt file. Status is OK if response
status HTTP 200 and there is more than month till expiration date.

# Usage

`python check_sites_health.py <path to a file>`

Example:

```#!bash

$ python check_sites_health.py urls.txt

http://vk.com -HTTP status is OK! (200)
http://vk.com - Domain paid!
http://mail.ru -HTTP status is OK! (200)
http://mail.ru - Domain paid!
http://facebook.com -HTTP status is OK! (200)
http://facebook.com - Domain paid!
http://ubuntu.ru -HTTP status is OK! (200)
http://ubuntu.ru - It's time to pay domain!

```

For help type:

`python check_sites_health.py --help`

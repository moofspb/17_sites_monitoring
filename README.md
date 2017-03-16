# Sites Monitoring Utility

Check status of sites from txt file. Status is OK if response
status HTTP 200 and there is more than month till expiration date.

# Usage

`python check_sites_health.py <path to a file>`

Example:

```#!bash

$ python check_sites_health.py urls.txt

'http://google.com' - OK
'http://amazon.com' - OK
'http://mail.ru' - It's time to pay domain!
'http://ulmart.ru' - OK
'http://avito.ru' - Can't get an expiration date!
'http://airbnb.com' - OK
'http://afllas.com' - No connection!
'http://booking.com' - OK
'http://youtube.com' - No connection!
'http://devman.org' - OK

```

For help type:

`python check_sites_health.py --help`

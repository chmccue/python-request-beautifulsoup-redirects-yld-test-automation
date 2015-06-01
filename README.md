# redirect_script_no_selenium
A more elegant, faster and efficient redirect testing script that does not require Selenium.

Dependencies:
Ensure these are installed -

-Python 2.7 (www.python.org/downloads)

-Python library Beautiful Soup 4.  To install with pip, from command line enter $ pip install beautifulsoup4

-Python library Requests.  To install with pip, from command line enter $ pip install requests

1.  Ensure that files "yld_cpo_list.py" and "YLD-num_region_market_url.csv" files are in the same directory/location as "redirects_v3.py" file.
2.  From command line, in location of the files, enter $ python redirects_v3.py
3.  File should begin running example, and output should be visible in the command line.  Example runs over 100 url redirect checks.  Run length depends on the computer speed and internet connection of the computer, but for average computer it should be completed in less than a minute.

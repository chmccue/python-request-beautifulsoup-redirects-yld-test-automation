import csv, os

# Import the csv file for markets and compile it into a list.
marketToURLFile = open(os.path.dirname(os.path.abspath(__file__)) + r"/YLD-num_region_market_url.csv")
csv_a = csv.reader(marketToURLFile)
marketCompareList = []
for row in csv_a:
    marketCompareList.append(row[0:4])


# These are lists that can be imported into the script.  old_url_list would have the old url that is expected to 
# redirect, while expected_url_list is where the old url is expected to redirect to.
old_url_list = []
expected_url_list = []


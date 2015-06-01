from bs4 import BeautifulSoup
import requests, unittest
from yld_cpo_list import marketCompareList as marketCompareList


BASE_URL = "http://www.yourlexusdealer.com/"
OLD_URL = "CPO"
NEW_URL = "lcertified/"
        
class MyRedirectTest(unittest.TestCase):
    def setUp(self):
        self.fail_count = 0
        self.fail_list = []
        print "Start of redirect test." 
        #pprint(self.json_dict_values)
        #print "\n"
        
    def tearDown(self):
        print "FAIL COUNT: %d" %self.fail_count
        if self.fail_count > 0:
            print "FAIL LIST: "
            for item in self.fail_list:
                print item
        #print self.fail_list
        print "\nTest case completed.  Examine above output for any FAILs. \n\n"
        
    def test_redirects_review(self):
        print "\nTest Case:  Redirect test\n"
        for num,region,marketName,marketURL in marketCompareList:
            username = ""
            password = ""
            original_url = BASE_URL+marketURL+OLD_URL
            expected_url = BASE_URL+marketURL+NEW_URL
            page = requests.get(original_url,auth = (username, password))
            soup = BeautifulSoup(page.content)
            print num
            try:
                r = page.status_code
                redirected_page_title = soup.title.text
                redirected_url = page.url
                redirect_status_list = []
                for resp in page.history:
                    redirect_status_list.append(str(resp.status_code))
                if r == 200 and redirected_url == expected_url:
                    print "Market: %s, Actual URL: %s" %(marketName, redirected_url)
                    print "actual page title: %s" %redirected_page_title
                    print "PASS - HTTP Status Code came back correct as %d" %(r)
                    print "HTTP Redirect Status Code: " + str(redirect_status_list)
                else:
                    self.fail_count += 1
                    self.fail_list.append([num,region,marketName,
                                           "actual page title: %s" %redirected_page_title,
                                           "HTTP Status Code: %d" %r,
                                           "HTTP Redirect Status Code: " + str(redirect_status_list),
                                           " entered URL: %s" %original_url,
                                           "expected URL: %s" %expected_url,
                                           "  actual URL: %s" %redirected_url])
                    print "POSSIBLE FAIL OR ERROR: HTTP Status Code %d" %(r) 
                    print "HTTP Redirect Status Code: " + str(redirect_status_list)
                    print "Or actual URL below does not match expected URL."
                    print "Region: %s" %region
                    print "Market: %s" %marketName
                    print "actual page title: %s" %redirected_page_title
                    print " entered URL: %s" %original_url
                    print "expected URL: %s" %expected_url
                    print "  actual URL: %s" % redirected_url
                    print "FAIL*******************************************************************************FAIL"
            except AssertionError:
                self.fail_count += 1
                print "Exception received while verifying HTTP Status Code.  Check link manually for more information."
                print "POSSIBLE FAIL OR ERROR: HTTP Status Code %d" %(r) 
                print "HTTP Redirect Status Code: " + str(redirect_status_list)
                print "FAIL*******************************************************************************FAIL"
            print "\n"
            
if __name__ == "__main__":
    unittest.main()

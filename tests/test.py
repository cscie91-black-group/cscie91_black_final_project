import urllib2, re
import unittest
from HTMLParser import HTMLParser

# Dynamically generate dev URL.

def generate_request_url():
    url = ''
    pat = re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

    try:
        # Get URL
        response = urllib2.urlopen('url to dev ip')
        # Get the code
        content = response.read()
        print "DEV ip: ", content
        matches = pat.match(content)
        if matches:
            devip = matches.group(0)
            url = "http://%s" % devip

    except urllib2.HTTPError as e:
        print e, 'while fetching ', url
        return
    return url


# function to get html data
def get_html_data():
    url = ''
    try:
        # Get URLs
        url = generate_request_url()
        response = urllib2.urlopen(url)
        print "The URL is: ", response.geturl()
        # Get the code
        print "This gets the code: ", response.code
        # Get all data
        html = response.read()
    except urllib2.HTTPError as e:
        print e, 'while fetching', url
        return

    parser = MyHTMLParser()
    parser.feed(html)
    content = parser.data
    parser.close()
    return content


# function to fetch status code
def get_status_code():
    try:
        # Get URLs
        url = generate_request_url()
        response = urllib2.urlopen(url)
        print "The URL is: ", response.geturl()
        # Get the code
        print "This gets the code: ", response.code
        return response.code

    except urllib2.HTTPError as e:
        print e, 'while fetching', url
        return


# Unit Tests
class Test(unittest.TestCase):
    def setUp(self):
        self.response_code = 0
        self.response_data = ''

    def test_content(self):
        self.response_data = get_html_data()
        self.assertEqual(self.response_data, '')

    def test_status_code(self):
        self.response_code = get_status_code()
        self.assertEqual(self.response_code, 200)


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ''

    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data
        self.data = data


if __name__ == "__main__":
    # start unit tests
    unittest.main()

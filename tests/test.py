import unittest, json, re
from urllib import request, parse
from html.parser import HTMLParser

# function to get html data
def get_html_data():
    data = None
    with open('index.html') as file:
        data = file.read()

    return data

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = ''
        self.img_count = 0
        self.group_members = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            # when we see an <img> increase count by 1
            self.img_count += 1

    def handle_endtag(self, tag):
        # h1 tags are only used to display group member names
        if tag == 'h1':
            # remove all except space characters and alpha characters
            data = re.sub(r'([^\s\w]|_)+', '', self.data)
            # strip all spaces before and after alpha characters
            data = data.strip()
            # make all chars lowercase
            data = data.lower()
            # append to group_members list
            self.group_members.append(data) 

    def handle_data(self, data):
        self.data = data

# Unit Tests
class Test(unittest.TestCase):
    def setUp(self):
        self.img_count = 3
        self.group_members = ['ethan haynes', 'sanu ann abraham', 'jim depina']
        self.messages = dict(messages=[])

    def test_content_is_valid(self):
        # get the data from our index.html 
        body = get_html_data()
        
        # build the request object to validate html against w3 validator api
        req = request.Request(
            'https://validator.w3.org/nu/?out=json', 
            data=body.encode('utf-8')
        )
        
        # pass content type of html in header
        req.add_header("Content-Type", "text/html")
        
        # make request
        res = request.urlopen(req)
        
        # parse json response object
        data = json.loads(res.read())
        
        # check that there aren't any errors
        self.assertEqual(data, self.messages)

    def test_html_content(self):
        # get the data from our index.html 
        body = get_html_data()
        
        # initialize our parser
        parser = MyHTMLParser()
        # pass in our index.html body string
        parser.feed(body)

        # check the <img> count is 3
        self.assertEqual(parser.img_count, self.img_count)
        # check that all of our names are present
        self.assertEqual(parser.group_members, self.group_members)


if __name__ == "__main__":
    # start unit tests
    unittest.main()

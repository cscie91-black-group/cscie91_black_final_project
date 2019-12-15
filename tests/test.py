import urllib2, re

# Dynamically generate dev URL.

def generate_request_url():
    url = ''
    pat = re.compile("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")

    try:
        # Get URL
        response = urllib2.urlopen('url to dev ip')
        # Get the code
        content = response.read()
        print("DEV ip: ", content)
        matches = pat.match(content)
        if matches:
            devip = matches.group(0)
            url = "http://%s" % devip

    except urllib2.HTTPError as e:
        print(e, 'while fetching ', url)
        return
    return url


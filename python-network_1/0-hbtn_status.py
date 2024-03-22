#!/usr/bin/python3
<<<<<<< HEAD
"""a Python script that fetches https://alu-intranet.hbtn.io/status"""


import urllib.request


if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
=======
import urllib.request

url = 'https://alu-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode("utf-8"))
>>>>>>> c5e0dc0645ac422ecb29558d225c4dca80283934

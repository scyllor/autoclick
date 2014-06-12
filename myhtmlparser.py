#!/usr/bin/python
#FileName : myhtmlparser

from HTMLParser import HTMLParser
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.links = []
        HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            if len(attrs) == 0:
                pass
            else:
                for(variable,value) in attrs:
                    if variable == 'href':
                        self.links.append(value)

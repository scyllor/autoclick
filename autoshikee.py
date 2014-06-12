#!/usr/bin/env python2.7
#Filename : autoshikee.py
#encoding: UTF-8

import urllib
import sys
import urllib2
import cookielib
from HTMLParser import HTMLParser
import re
import zlib
from StringIO import StringIO
from pyquery import PyQuery as pq
from myhtmlparser import MyHTMLParser
import gzip
import hashlib
import time

cj = cookielib.LWPCookieJar()
cookieSupport= urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
urllib2.install_opener(opener)
myurls = []
lastdigest = ''
lasturl = ''
md5 = hashlib.md5()

def login(username, password):
    headers = {
	    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
	    'Referer' : 'http://www.shikee.com/',
        'Accept'  :	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Encoding':'deflate',
	    'Accept-Language':	'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0',
	    'Connection':	'keep-alive',
	    'Host':	'login.shikee.com',
	    'Referer' :	'http://www.shikee.com/',
	    'User-Agent' :	'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
    }
    get('http://login.shikee.com')
    postData = {
	    'act':'alogin',
	    'password':password,
	    'username':username,
	    'to':'http:://www.shikee.com/'
    }
    print 'is login?' + str(post('http://login.shikee.com/login/check/1400484571',postData))


def post(url, postData):
    headers = {
	    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
	    'Referer' : 'http://www.shikee.com/',
        'Accept'  :	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	    'Accept-Encoding':'deflate',
	    'Accept-Language':	'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0',
	    'Connection':	'keep-alive',
	    'Host':	'login.shikee.com',
	    'Referer' :	'http://www.shikee.com/',
	    'User-Agent' :	'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
    }
    postData = urllib.urlencode(postData)
    request = urllib2.Request(url, postData, headers)
    response = urllib2.urlopen(request)
    return gzipdet(response)

def get(url):
    try:
        return gzipdet(urllib2.urlopen(url))
    except:
        print 'visit ' + url +' is error'

def gzipdet(response):
    gzipped = response.headers.get('Content-Encoding')
   #print 'isgzipped? ' + str(gzipped)
    if gzipped == 'gzip':
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj = buf)
        return f.read()
    else:
        return response.read()

def fetch(furl):
    print 'fetch ' + furl + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    wwwp = re.compile(r'(http://)?([^/]*)(/?.*)(\d{6})')
    #html = get(url)
    html = pq(url=furl)('.maxPicList').html()
    #md5.update(html.encode('utf8'))
    #keytxt = md5.hexdigest()
    #global lastdigest
    #print lastdigest
    #if lastdigest == keytxt:
    #    return
    #lastdigest = keytxt
    if html:
        hp = MyHTMLParser()
        hp.feed(html)
        hp.close()
        for link in hp.links:
            m = wwwp.match(link)
            if m:
                m.group(4)
                myurls.append(m.group(1)+m.group(2)+'/detail/apply/'+m.group(4)+'/?callback=?')

def clickitem(urls):
    global lasturl
    count = 0
    for url in urls:
        if url == lasturl:
            break
        if count == 10:
            count = 0
            break
        html = get(url)
        count += 1
        print 'click ' + str(count) + 'item ' +url
    if urls:
        lasturl = urls[1]

login('scyllor', 'hdliurui1234')
while True:
    time.sleep(0.5)
    try:
        fetch(sys.argv[1])
        clickitem(myurls)
    except:
        print 'An error occur, carry on boy!'
    myurls = []

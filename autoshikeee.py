#!/usr/bin/env python2.7
#Filename : autoshikeee.py
#encoding: UTF-8

import mechanize
import cookielib

#get browser entity
def getBrowser():
    # Browser
    br = mechanize.Browser()

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [
    ('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'),
    ('Referer','http://www.shikee.com/'),
    ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    ('Accept-Encoding','deflate'),
    ('Accept-Language','zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0'),
    ('Connection','keep-alive'),
    ('Host','login.shikee.com'),
    ('Referer','http://www.shikee.com/')]
    return br

#get Browser
br = getBrowser()

#login
def login(username, password, br):
    resp = br.open('http://login.shikee.com')
    html = resp.read()
    getFormByid(br)
    br.form['username'] = username
    br.form['password'] = password
    resp = br.submit()
    print resp.read()

#get form by id
def getFormByid(br):
    br.form = list(br.forms())[0]
    print br.form

#login
login('me@scylla.me', 'hdliurui1234', br)

# Looking at some results in link format
#for l in br.links(url_regex='stockrt'):
#    print l


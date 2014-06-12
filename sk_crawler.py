#!/usr/bin/python
#Filename : crawler.py

 
import urllib
import urllib2
import cookielib
import sys 
import chardet

hostUrl = "http://login.shikee.com/login/check" 
 
tbLoginUrl = "http://login.shikee.com"
 
cj = cookielib.LWPCookieJar() 
cookieSupport= urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
urllib2.install_opener(opener)
 
shikee = urllib2.urlopen(tbLoginUrl)
curl = shikee.geturl()
print curl
headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
	'Referer' : 'http://www.shikee.com/',
    	'Accept'  :	'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':	'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0',
	'Connection':	'keep-alive',
	'Host':	'login.shikee.com',
	'Referer' :	'http://www.shikee.com/',
	'User-Agent' :	'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
	
}
password = "hdliurui1234"
username = "scyllor"
postData = {
    'act': 'qlogin',  
    'password':password,
    'save_nl':'1',
    'to':'http://www.shikee.com/',
    'username':username
}
postData = urllib.urlencode(postData)
request = urllib2.Request(tbLoginUrl, postData, headers)
print type(request)
response = urllib2.urlopen(request)
url = response.geturl()
text = response.read()
info = response.info()
status = response.getcode()
typeEncode = sys.getfilesystemencoding()
infoencode = chardet.detect(text).get('encoding','utf-8')
print status,url,info
print text,text.decode(infoencode,'ignore').encode(typeEncode)

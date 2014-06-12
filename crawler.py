#!/usr/bin/python
#Filename : crawler.py

# -*- coding: utf-8 -*-
 
import urllib
import urllib2
import cookielib
 
hostUrl = "https://login.shikee.com/login/check" 
#此处不明白，不知道下载cookie主机地址，因此使用登录界面地址
 
tbLoginUrl = "https://login.taobao.com/member/login.jhtml"
 
#cookie 自动处理器
cj = cookielib.LWPCookieJar() #LWPCookieJar提供可读写操作的cookie文件,存储cookie对象
cookieSupport= urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookieSupport, urllib2.HTTPHandler)
urllib2.install_opener(opener)
 
#打开登陆页面
taobao = urllib2.urlopen(tbLoginUrl)
curl = taobao.geturl()
print curl
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',  
    'Referer' : '******'
}
password = "" #你的用户名和密码
username = ""
postData = {
    'CtrlVersion': '1,0,0,7',  
    'TPL_password':password,  
    'TPL_redirect_url':'',  
    'TPL_username':username,  
    #'_tb_token_':'I262PYW48um', 
    'action':'Authenticator',  
    'callback':'jsonp312',  
    'css_style':'',  
    'event_submit_do_login':'anything',  
    'fc':2,  
    'from':'tb',  
    'from_encoding':'',  
    'guf':'',  
    'gvfdcname':'',  
    'isIgnore':'',  
    'llnick':'',  
    'loginType':3,  
    'longLogin':0,  
    'minipara' :'',  
    'minititle':'',  
    'need_sign':'',  
    'need_user_id':'',  
    'not_duplite_str':'',  
    'popid':'',  
    'poy':'',  
    'pstrong':'',  
    'sign':'',  
    'style':'default',  
    'support':'000001',  
    'tid':''         
}
#编码
postData = urllib.urlencode(postData)
#发送请求
request = urllib2.Request(tbLoginUrl, postData, headers)
print type(request)
response = urllib2.urlopen(request)
#查看响应结果
url = response.geturl()
text = response.read()#为str类型，但是尝试使用 gbk , ascii解码都不正确，无法输出，暂时没想到解决办法
#原来是编辑器的原因，改用eclipse或者python IDE运行，结果如下
info = response.info()
status = response.getcode()
print status,url,info
print text

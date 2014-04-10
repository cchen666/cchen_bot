#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib,urllib2,httplib,cookielib

class Login:
    def __init__(self,url_slf):
        # init function has one parameter which is salesforce's url.

        # set cookie
        self.url_hi = url_slf
       
    def autologin(self,url,name,password):

        # url is for case's report url, name and pwd is salesforce account's name and pwd.

        cookie=cookielib.CookieJar()
        cj=urllib2.HTTPCookieProcessor(cookie)
        # set login parameter and use filebug to observe the data which is posted
        postdata=urllib.urlencode({'un':name,'pw':password})
        # form a request
        request=urllib2.Request(self.url_hi,postdata)
        # login
        opener=urllib2.build_opener(cj)
        f=opener.open(request)
        # open url
        hi_html=opener.open(url)
        return hi_html



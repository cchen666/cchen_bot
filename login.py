# -*- coding: utf-8 -*-
import urllib,urllib2,httplib,cookielib
#import xml.etree.ElementTree as ET
import xml.dom.minidom
from pyquery import PyQuery as pq




def auto_login_hi(url,name,pwd):
    url_hi="https://login.salesforce.com/"
    # set cookie
    cookie=cookielib.CookieJar()
    cj=urllib2.HTTPCookieProcessor(cookie)
    # set login parameter
    postdata=urllib.urlencode({'un':name,'pw':password})
    # form a request
    request=urllib2.Request(url_hi,postdata)
    # login
    opener=urllib2.build_opener(cj)
    f=opener.open(request)
    # open url
    hi_html=opener.open(url)
    return hi_html

def xmlhandle(h):

#    parser = ET.XMLParser(encoding="utf-8")
#    root = ET.fromstring(xmlori,parser=parser)
#    root=ET.parse(xmlori,parser=parser)
#    lst_node = root.getiterator("td")
#    for i in lst_node:
#        print_node(i)

#   doc = xml.dom.minidom.parseString(xmlori)
#   for node in doc.getElementsByTagName(tr):
#       print node.getAttribute("td")

    report = pg(h)
    



if __name__=='__main__':
    name=''
    password=''
    url='https://na7.salesforce.com/00OA00000056htR'
    h=auto_login_hi(url,name,password)
    report = pq(h.read().decode("UTF-8"))
    start=16 # The start num of 
#    print report('table .reportTable tabularReportTable').text()
    print report('tr').eq(start).find('td').text()
#    xmlhandle(h.read())


    



    

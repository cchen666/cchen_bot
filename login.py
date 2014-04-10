# -*- coding: utf-8 -*-
import urllib,urllib2,httplib,cookielib
#import xml.etree.ElementTree as ET
import xml.dom.minidom
from pyquery import PyQuery as pq


def auto_login_hi(url,name,pwd):

'''
This is a function for get the xml and cookie of salesforce.com
'''


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
    
'''
This function is used to grasp the case information from the xml file using pyquery.
'''

    report = pq(h)
    start=16             # The start num of tr
    count = 0            # The count of cases
    array=[[]]           # The array to save case Num, case SBT, case Sev, Case Title
    while (report('tr').eq(start).find('td').text() != None and report('tr').eq(start).find('td').eq(2).text()!=None):
        array.append([report('tr').eq(start).find('td').eq(2).text(),report('tr').eq(start).find('td').eq(5).text(),report('tr').eq(start).find('td').eq(11).text(),report('tr').eq(start).find('td').eq(1).text()])      # From the xml file, the tr should start with 16. And 2,5,11,1 stands for Num, SBT, Sev, Title
        start +=1
        count +=1
    return array,count
    
def output(content,num):

'''
A test function for output.
'''

    for i in range(1,num+1):
        print '%10s %8s %-12s %s' %(content[i][0],content[i][1],content[i][2],content[i][3])


if __name__=='__main__':
    name='cchen@redhat.com'
    password='52myself'
    url='https://na7.salesforce.com/00OA00000056htR'
    h=auto_login_hi(url,name,password)
    content,num = xmlhandle(h.read().decode("UTF-8")) 
    output(content,num)
    



    



    

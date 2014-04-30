#!/usr/bin/python
# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
import ConfigParser
import getpass
import login
import string
import time

class Xmlhandler:
    def __init__(self):
        self.count = 0
        self.start = 16
        self.array = [[]]

    def parser(self,h):
        report = pq(h)
        
        while (report('tr').eq(self.start).find('td').text() != '' and report('tr').eq(self.start).find('td').eq(2).text()!='' and report('tr').eq(self.start).find('td').text() != None and report('tr').eq(self.start).find('td').eq(2).text() != None):  # To ensure the case is not NULL or None

            self.array.append([report('tr').eq(self.start).find('td').eq(2).text(),report('tr').eq(self.start).find('td').eq(5).text(),report('tr').eq(self.start).find('td').eq(11).text(),report('tr').eq(self.start).find('td').eq(1).text()])      # From the xml file, the tr should start with 16. And 2,5,11,1 stands for Num, SBT, Sev, Title
            time.sleep(1)
            self.start +=1
            self.count +=1
        return self.array,self.count # We return two values: the 2-array with the case content and the number of new cases.


    def sortarr(self,array,index):
        '''
        sort the array. we sort the array according to the index.
        We copy the index and append it to the first column. 
        '''
        num = len(array)
        for i in range(0,num):
            array[i].insert(0,array[i][index])
            array[i][0]=string.atoi(array[i][0].replace(',',''))

        array.sort()
        for i in range(0,num):
            print array[i][0]
            del array[i][0]
        return array

if __name__=='__main__':

# test program 
    cp = ConfigParser.ConfigParser() 
    cp.read("dummy.conf") # read the config from dummy.conf
    name = cp.get("login","name")
    url = cp.get("login","url")
    password = getpass.getpass("Enter %s's password: " %name)

    # Finishing reading the config

    # Create a newlogin which is an instance of login ( we imported it )

    newlogin = login.Login("https://login.salesforce.com/")

    # autologin will return the xml's url
    content = newlogin.autologin(url,name,password)
    # Create a xmlhandler instance
    xmlh = Xmlhandler()
    # parser function will help us get the 2-array content and the count of new cases
    array,num = xmlh.parser(content.read().decode("UTF-8"))
    print array
    print num

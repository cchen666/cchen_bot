#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading  
import time  
import xmlhandler
import login
import gl
import time
import os
import signal
import getpass

class sc_thread(threading.Thread): #The sc_thread class is derived from the class threading.Thread  
    def __init__(self, num, interval, c,channel):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
        self.c = c
        self.channel=channel
        self.c.privmsg(self.channel,"Please Input the %s's salesforce password in terminal" %gl.name)
        self.password = getpass.getpass("Enter %s's salesforce password: " %gl.name)
        
    def run(self): #Overwrite run() method, put what you want the thread do here  

        for i in xrange(self.thread_num):  
            newlogin = login.Login("https://login.salesforce.com/")
            content = newlogin.autologin(gl.url,gl.name,self.password)
   #         print content.read()
            xmlh = xmlhandler.Xmlhandler()
            array1,num = xmlh.parser(content.read().decode("UTF-8"))
            del array1[0]
            array = xmlh.sortarr(array1,1)

            self.c.privmsg(self.channel,"============ JP New Case Queue ============")
            for i in range(0,num):
                tmp = '%9s %7s %-12s %s         %s' %(array[i][0],array[i][1],array[i][2],array[i][3],array[i][4])
                self.c.privmsg(self.channel,tmp)
                print tmp
            time.sleep(self.interval) 

    def stop(self):  
        self.thread_stop = True  
             
       
def test():  
        thread1 = sc_thread(5, 1, "c")
        thread1.start()
        return  
       
if __name__ == '__main__':  
        test()  

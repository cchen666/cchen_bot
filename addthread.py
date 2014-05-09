#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading  
import time  

class add_thread(threading.Thread):
    def __init__(self,num,interval,c,channel,op,user):
        threading.Thread.__init__(self)
        self.num = num
        self.interval = interval
        self.c = c
        self.channel = channel
        self.op = op
        self.user = user

    def run(self):
        if self.op == "add":
            for i in xrange(self.num):
                tmp = self.user+"++"
                self.c.privmsg(self.channel,tmp)
                time.sleep(self.interval)
            
        if self.op == "minus":
            for i in xrange(self.num):
                tmp = self.user+"--"
                self.c.privmsg(self.channel,tmp)
                time.sleep(self.interval)

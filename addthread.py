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
        self.whitelist = ["cchen","cchenlp","cchen-bot","Chen"]

    def run(self):
        if self.op == "add":
            if self.user not in self.whitelist:
                self.c.privmsg(self.channel,"Hi dude, if you want to add someone who is not in whitelist, please contact cchen for details")
            else:
                for i in xrange(self.num):
                    tmp = self.user+"++"
                    self.c.privmsg(self.channel,tmp)
                    time.sleep(self.interval)
            
        if self.op == "minus":
            if self.user == "cchen":
                self.c.privmsg(self.channel,"cchen: Master, some dog is tring to do something evil!")
            else:
                for i in xrange(self.num):
                    tmp = self.user+"--"
                    self.c.privmsg(self.channel,tmp)
                    time.sleep(self.interval)

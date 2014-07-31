#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading  
import time  

class enf_thread(threading.Thread):
    def __init__(self,c,case,nick):
        threading.Thread.__init__(self)
        self.case = case
        self.c = c
        self.nick = nick

    def run(self):

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A file that is used to save global variable read from configratuion file (dummy.conf).

import ConfigParser

cp = ConfigParser.ConfigParser()
cp.read("dummy.conf")
channel=cp.get("bot","channel")
server=cp.get("bot","server")
nickname=cp.get("bot","nickname")
name = cp.get("login","name")
url = cp.get("login","url")
#password = getpass.getpass("Enter %s's password: " %name)

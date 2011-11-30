#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: noet sts=4:ts=4:sw=4
# author: takano32
#

import sys
#sys.path.append('/usr/lib/pymodules/python2.5')
#sys.path.append('/usr/lib/pymodules/python2.5/gtk-2.0')

import os
os.environ['DISPLAY'] = ":32"
os.environ['XAUTHORITY'] = "/home/takano32/.Xauthority"

ROOM="#yuiseki/$4425ae72bc11c305"

import Skype4Py

import feedparser
d = feedparser.parse("http://pipes.yahoo.com/pipes/pipe.run?_id=8f34c1abdb8fc99e9aa057fac8e510e1&_render=rss")

def handler(msg, event):
	pass

skype = Skype4Py.Skype()
skype.OnMessageStatus = handler
skype.Attach()

room = skype.Chat(ROOM)

for item in d['items'][:5]:
    text = item.title + "\n" + item.link
	room.SendMessage(text)



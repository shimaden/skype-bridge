#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: noet sts=4:ts=4:sw=4
# author: takano32 <tak@no32 dot tk>
#

# Skype START
from configobj import ConfigObj
CONFIG = ConfigObj('../skype-bridge.conf')
ROOM = "#yuiseki/$4425ae72bc11c305"

import xmlrpclib
xmlrpc_host = CONFIG['bot']['xmlrpc_host']
xmlrpc_port = CONFIG['bot']['xmlrpc_port']
DAEMON = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_host, xmlrpc_port))
# Skype END

text = []
text.append('(devil) 戰じゃ〜！出陣せよ〜！ (devil)')
text.append('7:00~8:00 / 12:00~13:00 / 19:00~20:00 / 22:00~23:00')

DAEMON.send_message(ROOM, "\n".join(text))


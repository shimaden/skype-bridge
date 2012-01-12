#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: noet sts=4:ts=4:sw=4
# author: takano32 <tak@no32 dot tk>
#

codes = ['TYO:3632', 'TYO:2432']

import urllib2
from BeautifulSoup import BeautifulSoup
import re

# Skype START
from configobj import ConfigObj
CONFIG = ConfigObj('skype-bridge.conf')

import xmlrpclib
xmlrpc_host = CONFIG['bot']['xmlrpc_host']
xmlrpc_port = CONFIG['bot']['xmlrpc_port']
DAEMON = xmlrpclib.ServerProxy('http://%s:%s' % (xmlrpc_host, xmlrpc_port))
# Skype END

opener = urllib2.build_opener()

for code in codes:
	html = opener.open('http://www.google.com/finance?q=' + code).read()
	soup = BeautifulSoup(html)
	com = soup.find('h3').text.replace('&nbsp;', '')
	l  = soup.find(id = re.compile('ref_[0-9]+_l')).text
	c  = soup.find(id = re.compile('ref_[0-9]+_c')).text
	cp = soup.find(id = re.compile('ref_[0-9]+_cp')).text
	text = "[%s] %s %s JPY w/ %s %s" % (code, com, l, c, cp)
	DAEMON.send_message(ROOM, text)


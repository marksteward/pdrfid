#!/usr/bin/python

#  readtag.py - read all sectors from a standard tag
# 
#  Adam Laurie <adam@algroup.co.uk>
#  http://rfidiot.org/
# 
#  This code is copyright (c) Adam Laurie, 2006, All rights reserved.
#  For non-commercial use only, the following terms apply - for all other
#  uses, please contact the author:
#
#    This code is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This code is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#


import RFIDIOtconfig
import sys
import os
import socket
import time

try:
    card= RFIDIOtconfig.card
except:
    os._exit(True)

lastuid = None

print 'Card number: %s\n' % card.readernum

while True:
    
    #print 'Protocol: %s, %s\n' % (card.pcsc_protocol, card.pcsc_connection.getProtocol())
    card.select()
    if card.uid:

        if card.uid == lastuid:
            continue
        lastuid = card.uid

        print 'ID: %s\n' % card.uid

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('lovelace', 12346))
        s.send('Card %s %s;' % (card.readernum, card.uid))
        s.close()

    time.sleep(0.5)

os._exit(True)

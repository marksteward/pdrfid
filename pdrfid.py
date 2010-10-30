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

print 'Reader number: %s\n' % card.readernum

class PureData:

  def __init__(self, host):
    self.host = host
    self.port = 12346
    self.sock = None

  def connect(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    self.sock.connect((self.host, self.port))

  def newcard(self, readernum, uid):
    print 'Sending new card message for %s' % uid
    try:
      if self.sock is None:
        self.connect()

      self.sock.send('Card %s %s;' % (readernum, uid))

    except Exception, e:
      print 'Error %s sending message' % repr(e)
      self.sock.close()
      self.sock = None


pd = PureData('lovelace')

while True:
    
    #print 'Protocol: %s, %s\n' % (card.pcsc_protocol, card.pcsc_connection.getProtocol())
    card.select()
    if card.uid:

        if card.uid == lastuid:
            continue
        lastuid = card.uid

        print 'ID: %s\n' % card.uid
        pd.newcard(card.readernum, card.uid)

    time.sleep(0.5)

os._exit(True)



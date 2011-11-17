#!/usr/bin/python

import SimpleXMLRPCServer,sys

sys.path.append('/home/jfraser/svn/speed/phacter/trunk')

from phacter import phacter

class Phacter:
    def getFacts(self):
        p = phacter()
        return p.getFacts()

phacter_obj = Phacter()

server = SimpleXMLRPCServer.SimpleXMLRPCServer(('192.168.2.252',8888))
server.register_instance(phacter_obj)

print "Listening on port 8888"
server.serve_forever()


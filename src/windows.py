import os
import netifaces

def ipaddress():
    return netifaces.ifaddresses('{3351227E-DB77-4538-9524-2E59C6DAF564}')[2][0]['addr']
def fqdn():
    return 'server02.example.com'
def processorcount():
    return int(os.environ['NUMBER_OF_PROCESSORS'])

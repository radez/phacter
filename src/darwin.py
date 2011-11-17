import os
import netifaces

def ipaddress():
    return netifaces.ifaddresses('en0')[2][0]['addr']
def fqdn():
    return 'server02.example.com'
def processorcount():
    return int(os.popen('sysctl -n hw.ncpu').read())

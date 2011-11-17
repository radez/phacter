import os,netifaces
class Darwin:
    def ipaddress(self):
        return netifaces.ifaddresses('en0')[2][0]['addr']
    def fqdn(self):
        return 'server02.example.com'
    def processorcount(self):
        return int(os.popen('sysctl -n hw.ncpu').read())

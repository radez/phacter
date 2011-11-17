import os,netifaces
class Windows:
    def ipaddress(self):
        return netifaces.ifaddresses('{3351227E-DB77-4538-9524-2E59C6DAF564}')[2][0]['addr']
    def fqdn(self):
        return 'server02.example.com'
    def processorcount(self):
        return int(os.environ['NUMBER_OF_PROCESSORS'])

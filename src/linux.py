import netifaces
import platform
import os
import socket
import re
import subprocess
import md5
import uuid

from phacter import utils

def ipaddress():
    return netifaces.ifaddresses('eth0')[2][0]['addr']
def fqdn():
    return socket.gethostname()
def processorcount():
    return os.sysconf('SC_NPROCESSORS_ONLN')

def architecture():
    arch = platform.processor()
    if re.compile('i[3456]86').match(arch):
        return 'i386'
    else:
        return arch

def phacterversion():
    return '0.1'
def interfaces():
    i = netifaces.interfaces()
    return ",".join([n for n in i if 'lo' not in n])

def domain():
    return ".".join(socket.gethostname().split('.')[1:])
def hostname():
    return socket.gethostname().split('.')[0]
def hardwareisa():
    return platform.processor()
def hardwaremodel():
    return platform.processor()
def id():
    return os.environ['USER']
def pythonversion():
    return platform.python_version()
def kernelrelease():
    return platform.uname()[2]
def kernelversion():
    return platform.uname()[2].split('-')[0]
def lsbdistcodename():
    return os.popen('lsb_release -c').read().strip().replace('\t','').split(':')[1]
def lsbdistdescription():
    return os.popen('lsb_release -d').read().strip().replace('\t','').split(':')[1]
def lsbdistid():
    return os.popen('lsb_release -i').read().strip().replace('\t','').split(':')[1]
def lsbdistrelease():
    return os.popen('lsb_release -r').read().strip().replace('\t','').split(':')[1]
def lsbrelease():
    lsb_release = os.popen('lsb_release -v').read().strip().replace('\t','').split(':')[1:]
    return ":".join(lsb_release)
def lsbmajdistrelease():
    return os.popen('lsb_release -r').read().strip().replace('\t','').split(':')[1].split('.')[0]
def ps():
    return 'ps -ef'
def permid():
    m = md5.new(netifaces.ifaddresses('eth0')[17][0]['addr'].lower())
    return m.hexdigest()
def uuid():
    return str(uuid.uuid4())
def operatingsystem():
    l = Linux()
    lsbdistid = l.lsbdistid()
    if lsbdistid == 'Ubuntu':
        return lsbdistid
    elif os.path.isfile('/etc/debian_version'):
        return 'Debian'
    elif os.path.isfile('/etc/gentoo-release'):
        return 'Gentoo'
    elif os.path.isfile('/etc/fedora-release'):
        return 'Fedora'
    elif os.path.isfile('/etc/mandriva-release'):
        return 'Mandriva'
    elif os.path.isfile('/etc/mandrake-release'):
        return 'Mandrake'
    elif os.path.isfile('/etc/redhat-release'):
        f = open('/etc/redhat-release','r')
        if re.compile('centos',re.I).search(f.read()):
            return 'CentOS'
        else:
            return 'RedHat'
        f.close()
    elif os.path.isfile('/etc/SuSE-release'):
        f = open('/etc/SuSE-release','r')
        if re.compile('SUSE LINUX Enterprise Server',re.I).search(f.read()):
            return 'SLES'
        else:
            return 'SuSE'

def operatingsystemrelease():
    l = Linux()
    operatingsystem = l.operatingsystem()
    if operatingsystem == 'Debian':
        f = open('/etc/debian_version','r')
        v = f.read()
        f.close()
    return v
    elif operatingsystem == 'Gentoo':
        f = open('/etc/gentoo-release','r')
        v = f.read() 
        f.close()
        return v
    elif operatingsystem == 'Fedora':
        f = open('/etc/fedora-release','r')
        for line in f.readlines():
            if 'Rawhide' in line:
                value = 'Rawhide'
            elif 'release' in line:
                value = line
            else:
                value = 'Unknown'
        f.close()
        return value
    elif os.path.isfile('/etc/mandriva-release'):
        return 'Mandriva'
    elif os.path.isfile('/etc/mandrake-release'):
        return 'Mandrake'
    elif operatingsystem == 'CentOS':
        f = open('/etc/redhat-release','r')
        f.close()
        return '5.2'
    elif operatingsystem == 'RedHat':
        f = open('/etc/redhat-release','r')
        for line in f.readlines():
            if 'Rawhide' in line:
                value = 'Rawhide'
            elif 'release' in line:
                value = line
            else:
                value = 'Unknown'
        f.close()
        return value
    elif os.path.isfile('/etc/SuSE-release'):
        f = open('/etc/SuSE-release','r')
        if re.compile('SUSE LINUX Enterprise Server',re.I).search(f.read()):
            return 'SLES'
        else:
            return 'SuSE'

def manufacturer():
    if os.path.isfile('/usr/sbin/dmidecode'):
        s = subprocess.Popen(['/usr/sbin/dmidecode'],shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
        if 'Permission denied' in s.stderr.read():
            pass
        for line in s.stdout.readlines(): 
            if 'Manufacturer' in line:
                m = line.split(':')[1].strip()
                return m

def dealeraddress():
    u = utils()
    return ":".join(u.getDealerAddress())



#ipaddress_eth0
#macaddress
#macaddress_eth0
#macaddress_eth1
#memoryfree
#memorysize
#netmask
#netmask_eth0
#operatingsystemrelease
#processor0
#processor1
#rubysitedir
#sshdsakey
#sshrsakey
#swapfree
#swapsize
#virtual

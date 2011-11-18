# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import netifaces

def ipaddress():
    return netifaces.ifaddresses('en0')[2][0]['addr']
def fqdn():
    return 'server02.example.com'
def processorcount():
    return int(os.popen('sysctl -n hw.ncpu').read())

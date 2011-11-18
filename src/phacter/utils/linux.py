# This software may be freely redistributed under the terms of the GNU
# general public license.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import subprocess
def getDealerAddress():
        matches = []
        cmd = [ '/usr/bin/avahi-browse', '--all', '--terminate', '--resolve' ]
        cmdp = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE)
        data = cmdp.communicate()[0]
        lines = data.split('\n')
        match_mode = False
        for line in lines:
            if line.startswith("="):
                if line.find("dealer") != -1 and line.find('IPv4') != -1:
                    match_mode = True
                else:
                    match_mode = False
            if match_mode and line.find("address") != -1 and line.find("[") != -1:
                (afirst, alast) = line.split("[",1)
                (addr, junk) = alast.split("]",1)
                if addr.find(":") == -1:
                    matches.append(addr.strip())
            if match_mode and line.find("port") != -1 and line.find("[") != -1:
                (lfirst,llast) = line.split("[",1)
                (port,ljunk) = llast.split(']',1)
                matches.append(port.strip())

        #return matches
        return ('127.0.0.1','80')

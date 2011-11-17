#!/usr/bin/python
import platform,sys,urllib,httplib
platform_name = platform.system()
#import_module = __import__('speed.phacter.%s' % platform_name,globals(),locals(),['%s' % platform_name ])
#import_module = __import__('phacter.%s' % platform_name,globals(),locals(),['%s' % platform_name ])
import_module = __import__('%s' % platform_name,globals(),locals(),['%s' % platform_name ])


class phacter:

    def getFacts(self):
        platform_obj = getattr(import_module,platform_name)()

        facts = {}
        facts['kernel'] = platform_name

        for method in dir(platform_obj):
            if '__' not in method:
                answer = getattr(platform_obj,method)()
                if answer is not None:
                    facts[method] = answer
        
        return facts

    def updateFacts(self):
        f = self.getFacts()
        url = f['dealeraddress']
        params = urllib.urlencode(self.getFacts())
        headers = { "Content-type" : "application/x-www-form-urlencoded",
                    "Accept" : "text/plain" }
        conn = httplib.HTTPConnection(url)
        conn.request('POST','/index.php',params,headers)
        response = conn.getresponse()
        print response.status,response.reason
        data = response.read()
        conn.close
        return data
        


def main():
    p = phacter()
    f = p.getFacts()
    for (key,value) in f.items():
        print "%s => %s" % (key,value)
    u = p.updateFacts()
    print u
    
if __name__ == '__main__':
    main()

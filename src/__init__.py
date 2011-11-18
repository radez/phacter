#!/usr/bin/python
import platform
import sys
import urllib
import httplib

from types import ModuleType

class Lazy(object):
    def __init__(self, func):
        self._func = func

    def __get__(self, obj, _=None):
        if obj is None:
            return self
        value = self._func()
        setattr(obj, self._func.func_name, value)
        return value

class Phacter(object):

    facts = ['kernel']
    platform_name = platform.system().lower()
    kernel = property(lambda self: self.platform_name)

    def __init__(self):
        platform_imp = __import__('phacter', None, None, [self.platform_name])
        platform_obj = getattr(platform_imp, self.platform_name)

        for method in dir(platform_obj):
            if '__' not in method:
                call = getattr(platform_obj, method)
                if type(call) is not ModuleType:
                    setattr(self.__class__, method, Lazy(call))
                    self.facts.append(method)
        self.facts.sort()


if __name__ == 'phacter':
    sys.modules[__name__] = Phacter()

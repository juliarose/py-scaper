from requester.simple_get import simple_get
from os import path

class Site(object):
    def __init__(self, hostname):
        self.hostname = hostname
    
    def get(self, location):
        return simple_get('https://' + self.hostname + location)
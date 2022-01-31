import requests
import xml2dict as xml
from constants import *


class NBAPI:
    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password
        self.session = None
        self.command = {NETBOX: {SESSION: '900493538'}}

    def login(self):
        self.command[NETBOX][CMD] = login(self.username, self.password)
        req = requests.post(self.ip, self.command)
        self.command = {NETBOX: {SESSION: str(xml.parse(req)['NETBOX']['sessionid'])}}

    def add_person(self, first, last, access=None):
        self.command[NETBOX][CMD] = modify_user(ADDUSR, user(first, last, accesslevel=access))
        return self.command

    def mod_person(self, first, last, access=None):
        self.command[NETBOX][CMD] = modify_user(MODUSR, user(first, last, accesslevel=access))
        return self.command

    def del_person(self, first, last):
        self.command[NETBOX][CMD] = modify_user(DELUSR, user(first, last))
        return self.command

    def unlock_momentary(self, portal):
        self.command[NETBOX][CMD] = momentary(getportal(portal))
        return self.command

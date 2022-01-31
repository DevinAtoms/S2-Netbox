import xml2dict as xml
from util import NBAPI


session = NBAPI('127.0.0.1', 'admin', 'password')
s2xml = open('request.xml', 'r').read()
login = open('login.xml', 'r').read()

request = xml.parse(s2xml)

print(request)
print(session.unlock_momentary(7))

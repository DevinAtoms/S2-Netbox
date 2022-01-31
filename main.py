from util import APISession
# noinspection StandardLibraryXml
import xml.etree.ElementTree as ET

xmlfile = open('XML/GetPerson.xml', 'r').read()

session = APISession('0.0.0.0', 'user', 'password')
adduser = session.add_person('firstname', 'lastname')
elements = list(adduser['NETBOX-API'].keys())

root = ET.Element('NETBOX-API')
root.attrib['sessionid'] = '900493538'

command = ET.SubElement(root, 'COMMAND')
command.attrib['name'] = 'GetPerson'
command.attrib['num'] = '1'

params = ET.SubElement(command, 'PARAMS')
content = ET.SubElement(params, 'PERSONID').text = '123456'

ET.ElementTree(root).write('test.xml')

print()

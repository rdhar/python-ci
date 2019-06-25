from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import json
import sys

content = sys.stdin.read()
obj = json.loads(content, strict=True)
xml = dicttoxml(obj, attr_type=False, root=False)
dom = parseString(xml)
print(dom.toprettyxml())

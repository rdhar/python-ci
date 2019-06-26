from dump_xml import dump_xml
from xml.etree import ElementTree
import json
import sys

base_element_name = "base"
if len(sys.argv) >= 2:
    base_element_name = sys.argv[1]

string_repr = '\n'.join(sys.stdin.readlines())
dict_repr = json.loads(string_repr)
xml_tree = dump_xml(dict_repr, base_element_name)

print(ElementTree.tostring(xml_tree, encoding='unicode'))

import json
import urllib
import dicttoxml
from xml.dom.minidom import parseString

content = '{"num_failed": 20,"num_passed": 1024,"test_case0: rotational iterative": [{"actual": 420,"expected": 138,"name": "splicer swing buffer assertion0","passed": false},{"actual": 893,"expected": 72,"name": "randomification concurrency assertion1","passed": false},{"actual": 293,"expected": 189,"name": "FPU randomification assertion2","passed": false}],"test_case1: time progressive": [{"actual": 991,"expected": 970,"name": "concurrency symbolic assertion0","passed": false},{"actual": 807,"expected": 936,"name": "paths warp assertion1","passed": false},{"actual": 400,"expected": 389,"name": "matrices function assertion2","passed": false}],"test_name": "tracer_operating"}'
obj = json.loads(content, strict=False)
xml = dicttoxml.dicttoxml(obj, attr_type=False)
dom = parseString(xml)
print(dom.toprettyxml())

# '{"num_failed": 20,"num_passed": 1024,"test_case0: rotational iterative": [{"actual": 420,"expected": 138,"name": "splicer swing buffer assertion0","passed": false},{"actual": 893,"expected": 72,"name": "randomification concurrency assertion1","passed": false},{"actual": 293,"expected": 189,"name": "FPU randomification assertion2","passed": false}],"test_case1: time progressive": [{"actual": 991,"expected": 970,"name": "concurrency symbolic assertion0","passed": false},{"actual": 807,"expected": 936,"name": "paths warp assertion1","passed": false},{"actual": 400,"expected": 389,"name": "matrices function assertion2","passed": false}],"test_name": "tracer_operating"}'
# '{"mydict": {"foo": "bar", "baz": 1}, "mylist": ["foo", "bar", "baz"], "ok": true}'
# '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
# {u'mylist': [u'foo', u'bar', u'baz'], u'mydict': { u'foo': u'bar', u'baz': 1}, u'ok': True}

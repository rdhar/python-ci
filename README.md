# Python CI with Jenkins

## Commands

### Run a test file

```sh
python test_primes.py
```

### Generate J-Unit XML report of test results

```sh
pytest --pep8 --junitxml=results.xml --json-report --json-report-indent=4 --json-report-file=results.json || exit 0
```

### Generate linting log of all Python files
```sh
pylint_runner --rcfile=./.pylintrc > pylint.log || exit 0
```

### Convert from JSON to XML from command line
```sh
python convertJsonToXml.py < filename.json > filename.xml
```

### Convert from XML to JSON then from JSON back to XML
```sh
xml2json -d gdata results.xml > converted_results.json && convertJsonToXml.py < converted_results.json > converted_results.xml
```

### HTTP Post URL from Jenkin's Git Plugin

```md
http://localhost:5555/git/notifyCommit?url=file://D:/python-ci

from http://www.andyfrench.info/2015/03/automatically-triggering-jenkins-build.html
```


```py
# Sample JSON input data for 'content'
# '{"num_failed": 20,"num_passed": 1024,"test_case0: rotational iterative": [{"actual": 420,"expected": 138,"name": "splicer swing buffer assertion0","passed": false},{"actual": 893,"expected": 72,"name": "randomification concurrency assertion1","passed": false},{"actual": 293,"expected": 189,"name": "FPU randomification assertion2","passed": false}],"test_case1: time progressive": [{"actual": 991,"expected": 970,"name": "concurrency symbolic assertion0","passed": false},{"actual": 807,"expected": 936,"name": "paths warp assertion1","passed": false},{"actual": 400,"expected": 389,"name": "matrices function assertion2","passed": false}],"test_name": "tracer_operating"}'
# '{"mydict": {"foo": "bar", "baz": 1}, "mylist": ["foo", "bar", "baz"], "ok": true}'
# '{"login":"mojombo","id":1,"avatar_url":"https://avatars0.githubusercontent.com/u/1?v=4"}'
# '{u'mylist': [u'foo', u'bar', u'baz'], u'mydict': { u'foo': u'bar', u'baz': 1}, u'ok': True}'

# import xml.etree.cElementTree as ET
# element = ET.SubElement(document, 'testCase', classname=test_case_name_array[0] + "." + test_case_name_array[1],
#                         file=test_case_name_array[0], name=test_case_name_array[2], time=str(test_suite[i]["teardown"]["duration"]))
#     i = i + 1 -->
```

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

# Python CI with Jenkins

## Commands

### Run a test file

```sh
python test_primes.py
```

### Generate J-Unit XML report of test results

```sh
pytest --junitxml=D:\python-ci\results.xml
```

### HTTP Post URL from Jenkin's Git Plugin

```md
http://localhost:5555/git/notifyCommit?url=file://D:/python-ci

from http://www.andyfrench.info/2015/03/automatically-triggering-jenkins-build.html
```

import json
import random
import sys
import time
from random import randint

class genJsonTest():

    _testNames = [
        "compiler",
        "operating",
        "system",
        "magnetron",
        "simulation",
        "bundler",
        "path",
        "tracer",
        "emulation",
        "architecture",
        "framework",
        "meta",
        "modeling"
    ]

    _testCaseNames = [
        "fractal",
        "recursive",
        "stack",
        "iterative",
        "transverse",
        "rotational",
        "regressive",
        "aggressive",
        "watermark",
        "bandwidth",
        "memory",
        "time",
        "progressive",
        "combinatorial"
    ]

    _assertNames = [
        "integer",
        "boolean",
        "float",
        "function",
        "instance",
        "threading",
        "concurrency",
        "paths",
        "PPU",
        "FPU",
        "swing buffer",
        "symbolic",
        "semantic",
        "abstraction",
        "randomification",
        "splicer",
        "alternative",
        "optimisation",
        "entry point",
        "matrices",
        "flux",
        "warp",
        "driver"
    ]

    _randomTitles = [
        "Test Build : Cosmic Twin Test",
        "Test Build : Halcyon Ascent Test",
        "Test Build : Revelation Test",
        "Test Build : Sirius Test Suite",
        "Test Build : Leviathan Tempterature Test",
        "Test Build : Binary Polymorphism Test",
        "Test Build : PCUnderTemperatureCheck",
        "Test Build : 2938 Renegade Test",
        "Test Build : Evolution Test 1"
    ]

    _randomDescription = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Fusce mollis augue felis",
        "In hac habitasse platea dictumst.",
        "Fusce sodales congue commodo.",
        "Interdum et malesuada fames ac ante ipsum primis in faucibus.",
        "Aliquam turpis erat, interdum et mauris vitae, sagittis tempus lacus",
        "Aliquam egestas mauris sit amet ligula hendrerit maximus",
        "Sed vel tincidunt turpis, vitae posuere orci",
        "Nam eget ex vitae purus porttitor lacinia non ac elit",
        "Morbi eget sapien at metus tempor viverra at non erat",
        "Integer dictum quam eu pulvinar dignissim",
        "Mauris lorem odio, volutpat id bibendum et, rhoncus sit amet lorem",
        "hasellus iaculis velit magna, eget vulputate turpis lobortis ac",
        "Duis malesuada, augue a convallis hendrerit, velit augue posuere sapien",
        "Sed maximus ullamcorper consequat",
        "Ut non enim nec lacus maximus ornare",
        "Aenean porttitor faucibus eros id convallis",
        "Donec tempus, odio nec tempus ornare, risus mi blandit felis, id feugiat enim odio et tellus"

    ]


    def _randomName(self,source,count,seperator = ' ' ):
        pickName = lambda : source[(random.randrange(0, len(source)))]
        name = pickName()
        for i in range(1,count):
            name = "{0}{1}{2}".format(name, seperator, pickName() )
        return name

    def _getRandomDescription(self):
        return self._randomDescription[randint(0, len(self._randomDescription) - 1)]

    def _randomTestName(self):
        return self._randomName(self._testNames, 2, '_' )

    def _randomTestCaseName(self,index):
        return "test_case_{0}:".format(index + 1)

    def _randomAssertName(self):
        return self._randomName(self._assertNames, 2)


    def _randomTestCount(self):
        return random.randrange(3,8)

    def _randomTestCaseCount(self):
        return random.randrange(1,4)

    def _randomTestValue(self):
        return random.randrange(-128, 1024)

    def _randomTestPass(self):
        value = random.randrange(1,100)
        if value < 80:
            return "PASSED"
        else:
            return "FAILED"

    def _genMetaData(self, io):
        io["test"] = self._randomTitles[randint(0, len(self._randomTitles))]
        return io

    def _genTest(self, index):
        test = dict()

        #test["name"] = "{0}{1}{2}".format(self._randomAssertName(), " assertion", index)
        test["expected"] = self._randomTestValue()
        test["actual"] = self._randomTestValue()
        test["outcome"] = self._randomTestPass()
        test["number"] = str(randint(1,100))
        test["description"] = self._getRandomDescription()
        test["difference"] = str(int(test["actual"]) - int(test["expected"]) )
        return test

    def _genSummary(self):
        summary = dict()
        summary["check_count"] = 14
        summary["pass_count"] = 14
        summary["fail_count"] = 1
        summary["outcome"] = "FAILED"
        return summary

    def _genTestMeta(self, index, k, tests):
        test = self._genTest(k)
        tests["number"] = str(index + 1)
        tests["test_{0}".format(k)] = test
        tests["name"] = self._randomTitles[randint(0,len(self._randomTitles) - 1)]

    def _genTestCase(self, io, index):
        tests = {}
        k = 1
        i = randint(1,3)
        for i in range(0, self._randomTestCount()):
            self._genTestMeta( index, k, tests)
            k = k + 1
        io[self._randomTestCaseName(index)] = tests
        return io


    def generate(self):
        data = dict()
        data = self._genMetaData(data)
        for i in range(0, self._randomTestCaseCount()):
            data = self._genTestCase(data,i)
        data["summary"] = self._genSummary()
        return data

#end of class "genJsonTest"

def generateTests(count,seed=time.gmtime()):
    random.seed(seed)
    testGen = genJsonTest()
    for i in range(0,count):
        data = testGen.generate()
        fileName = "test{0}.json".format(i)
        with open(fileName, "w") as textFile:
            jsonString = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            textFile.write(jsonString)
            print("written file: {0}".format(fileName))

def main():

    if len(sys.argv) == 2:
        count = sys.argv[1]
        intCount = int(count)

        generateTests(intCount)
    else:
        print("Error: incorrect number of command line arguments")


if __name__ == '__main__':
    main()
    exit(0)
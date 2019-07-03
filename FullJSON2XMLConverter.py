import json
import xml.etree.cElementTree as ET
from io import BytesIO
import datetime
import sys
import os
import random


def read_json_file (json_file_name):
   json1_file = open(json_file_name)
   json1_str = json1_file.read()
   json1_dict = json.loads(json1_str)
   return json1_dict

def begin_document(test_suite, jason_dict):
    failure_count = test_suite["summary"]["fail_count"]
    skip_count = "0"
    error_count = test_suite["summary"]["fail_count"]
    if len(test_suite) > 0:
       document = ET.Element('testsuite', errors = "0", failures = str(failure_count), name = jason_dict["test"] , skipped = "0", tests = str(int(test_suite["summary"]["fail_count"]) + int(test_suite["summary"]["pass_count"])) , time = "0.499")
       return document
    else:
        print("The JSON file contains no items")
        exit()

def checkSubsystem():
    if len(sys.argv) > 1 :
        return sys.argv[1]
    else:
        print "There is an issue with the system argument add the subsystem of the test"
        return "There is an issue with the system argument add the subsystem of the test"

def add_tests(test_iterator, test_suite, test_case_ID, document, jason_dict):
    test_ID = "test_" + str(test_iterator + 1)
    test = test_suite[test_case_ID][test_ID]
    element = ET.SubElement(document, 'testcase',classname = str(jason_dict["test"]) , file = str(checkSubsystem()),line = str(random.randint(1, 1000)), name = str(jason_dict[test_case_ID]["name"]) + " " + test_ID, time = str(datetime.datetime.now()))
    if test["outcome"] == "FAILED":
        handle_failure(test,element)
            
def add_testcases(jason_dict):
    test_suite = jason_dict
    document = begin_document(test_suite, jason_dict)
    testCase_iterator = 0
    number_of_testcases = len(test_suite) - 2
    while testCase_iterator < number_of_testcases:
        test_case_ID = "test_case_" + str(testCase_iterator + 1) + ":"
        number_of_tests = len(test_suite[test_case_ID]) - 2
        test_iterator = 0
        while test_iterator < number_of_tests:
            add_tests(test_iterator, test_suite, test_case_ID, document, jason_dict)
            test_iterator = test_iterator + 1
        testCase_iterator = testCase_iterator + 1
    return document

def handle_failure(test, element):
        ET.SubElement(element, 'failure',message = test["description"], description = test["description"])

def count_errors(test_suite):
    count = 0
    i = 0
    while i < len(test_suite):
        if test_suite[i]["outcome"] == "error":
            count = count + 1
        i = i + 1
    return "1"

def count_skip(test_suite):
    count = 0
    i = 0
    while i < len(test_suite):
        if test_suite[i]["outcome"] == "skipped":
            count = count + 1
        i = i + 1
    return count

def test_case_processor(string):
    array = string.split("::")
    return array

def tree_builder(jason_dict):
   document = add_testcases(jason_dict)
   ET.SubElement(document, 'testcase')
   tree = ET.ElementTree(document)
   f = BytesIO()
   tree.write(f, encoding='utf-8', xml_declaration=True) 
   return f.getvalue()

def write_tree(tree):
    tree.write("customRecordLow.xml")

def write_string(string):
    if os.path.exists("TranslatedRecord.xml"):
       os.remove("TranslatedRecord.xml")
    xmlFile = open("TranslatedRecord.xml","w+")
    xmlFile.write(string)
    xmlFile.close()

def main():
    random.seed(1)
    jason_dict = read_json_file("test0.json")
    string = tree_builder(jason_dict)
    write_string(string)
   
if __name__== "__main__":
  main()
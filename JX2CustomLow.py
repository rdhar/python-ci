import json
import xml.etree.cElementTree as ET
from io import BytesIO
import dicttoxml


def read_json_file(json_file_name):
    json1_file = open(json_file_name)
    json1_str = json1_file.read()
    json1_dict = json.loads(json1_str)
    return json1_dict


def add_testcases(jason_dict):
    test_suite = jason_dict["report"]["tests"]
    failure_count = count_failures(test_suite)
    skip_count = count_failures(test_suite)
    error_count = count_errors(test_suite)
    if len(test_suite) > 0:
        document = ET.Element('testSuite', errors=str(error_count), failures=str(
            failure_count), name="JSON Translate", skipped=str(skip_count), tests=str(len(test_suite)), time="This needs to be added")
    i = 0
    while i < len(test_suite):

        test_case_name_array = test_case_processor(test_suite[i]["name"])

        element = ET.SubElement(document, 'testCase', classname=test_case_name_array[0] + "." + test_case_name_array[1],
                                file=test_case_name_array[0], name=test_case_name_array[2], time=str(test_suite[i]["teardown"]["duration"]))
        if test_suite[i]["outcome"] == "failed":
            handle_failure(test_suite, element)
        i = i + 1

    return document


def handle_failure(test_suite, element):
    ET.SubElement(element, 'Failcase', classname="lol")


def count_failures(test_suite):
    count = 0
    i = 0
    while i < len(test_suite):
        if test_suite[i]["outcome"] == "failed":
            count = count + 1
        i = i + 1
    return count


def count_errors(test_suite):
    count = 0
    i = 0
    while i < len(test_suite):
        if test_suite[i]["outcome"] == "error":
            count = count + 1
        i = i + 1
    return count


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

    ET.SubElement(document, 'testCase')

    tree = ET.ElementTree(document)

    f = BytesIO()
    tree.write(f, encoding='utf-8', xml_declaration=True)

    return f.getvalue()


def write_tree(tree):
    tree.write("customRecordLow.xml")


def write_string(string):
    xmlFile = open("customRecordLow.xml", "w+")
    xmlFile.write(string)
    xmlFile.close()


def main():
    jason_dict = read_json_file("report.json")

    string = tree_builder(jason_dict)
    write_string(string)


if __name__ == "__main__":
    main()

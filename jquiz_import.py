#!/usr/local/bin/python
import csv
from sys import argv


def read_csv(filename, fms):
    with open(filename, 'rb') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',', quotechar='|')
        next(csv_file, None)
        for row in csv_file:
            each_q = format_to_xml(fms, row)
            write_to_file(each_q)


def write_to_file(q):
    xml_file = argv[2]
    jquiz_file = open(xml_file, 'r')
    line = jquiz_file.readlines()
    jquiz_file.close()

    line.insert(27, q)

    jquiz_file = open(xml_file, "w")
    content = "".join(line)
    jquiz_file.write(content)
    jquiz_file.close()


def get_empty_template():
    return """
    <question-record>
                <question>{}</question>
                <clue></clue>
                <category></category>
                <weighting>100</weighting>
                <fixed>0</fixed>
                <question-type>{}</question-type>
                <answers>
                    <answer>
                        <text>{}</text>
                        <feedback></feedback>
                        <correct>{}</correct>
                        <percent-correct>0</percent-correct>
                        <include-in-mc-options>1</include-in-mc-options>
                    </answer>
                    <answer>
                        <text>{}</text>
                        <feedback></feedback>
                        <correct>{}</correct>
                        <percent-correct>100</percent-correct>
                        <include-in-mc-options>1</include-in-mc-options>
                    </answer>
                    <answer>
                        <text>{}</text>
                        <feedback></feedback>
                        <correct>{}</correct>
                        <percent-correct>0</percent-correct>
                        <include-in-mc-options>1</include-in-mc-options>
                    </answer>
                    <answer>
                        <text>{}</text>
                        <feedback></feedback>
                        <correct>{}</correct>
                        <percent-correct>0</percent-correct>
                        <include-in-mc-options>1</include-in-mc-options>
                    </answer>
                </answers>
            </question-record>
    """


def format_to_xml(fms, entry):
    return fms.format(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8],
                      entry[9])


def main():
    fms = get_empty_template()
    read_csv(argv[1], fms)


if __name__ == '__main__':
    main()

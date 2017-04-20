#!/usr/local/bin/python
import csv
from sys import argv


def read_csv(filename):
    with open(filename, 'rb') as csvfile:
        csv_file = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csv_file, None)  # Skips first line of .csv file
        for row in csv_file:
            num_of_as = (len(row) - 3) / 2
            answers = calc_weight(row, num_of_as)
            all_answers = fill_all(answers, num_of_as)
            final_question = fill_form(row, all_answers)
            write_to_file(final_question)


def calc_weight(entry, num_of_as):
    global value_of_true
    entry = entry[4:]
    value_of_true = float(entry.count("1"))
    value_of_false = - float(entry.count("0"))
    for i in range(num_of_as * 2):
        if i % 2 != 0:
            if "1" == entry[i]:
                entry[i] = check_zero(value_of_true)
            elif "0" == entry[i]:
                entry[i] = check_zero(value_of_false)
    return entry


def fill_all(answers, num_of_as):
    all_a = ""
    for i in range(num_of_as * 2):
        if i % 2 == 0 and answers[i] != "":
            each_a = fill_each_a(answers[i], answers[i + 1])
            all_a = all_a + each_a
    return all_a


def fill_each_a(answer, weight):
    empty_answer = get_empty_question()
    return empty_answer.format(weight, answer)


def fill_form(entry, answer):
    final_template = get_empty_template()
    return final_template.format(entry[0], entry[1], entry[2], answer)


def check_single():
    if value_of_true == 100.0:
        return "true"
    else:
        return "false"


def check_zero(value):
    if value != 0:
        return 1 / value * 100
    else:
        return 0


def write_to_file(content):
    xml_file = argv[2]
    final_file = open(xml_file, 'r')
    line = final_file.readlines()
    final_file.close()

    line.insert(2, content)

    final_file = open(xml_file, "w")
    content = "".join(line)
    final_file.write(content)
    final_file.close()


def get_empty_question():
    return """
    <answer fraction="{}" format="html">
        <text><![CDATA[<p>{}</p>]]></text>
        <feedback format="html">
            <text></text>
        </feedback>
    </answer>
    """


def get_empty_template():
    return """<!--question {} -->
<question type="multichoice">
    <name>
        <text>{}</text>
    </name>
    <questiontext format="html">
        <text><![CDATA[<p>{}</p>]]></text>
    </questiontext>
    <generalfeedback format="html">
        <text></text>
    </generalfeedback>
    <defaultgrade>1.0000000</defaultgrade>
    <penalty>0.3333333</penalty>
    <hidden>0</hidden>
    <single>false</single>
    <shuffleanswers>true</shuffleanswers>
    <answernumbering>abc</answernumbering>
    <correctfeedback format="html">
        <text><![CDATA[<p>Die Antwort ist richtig</p>]]></text>
    </correctfeedback>
    <partiallycorrectfeedback format="html">
        <text><![CDATA[<p>Die Antwort ist teilweise richtig.</p>]]></text>
    </partiallycorrectfeedback>
    <incorrectfeedback format="html">
        <text><![CDATA[<p>Die Antwort ist falsch</p>]]></text>
    </incorrectfeedback>
    <shownumcorrect/>
   {}
</question>
    """


def main():
    read_csv(argv[1])


if __name__ == '__main__':
    main()

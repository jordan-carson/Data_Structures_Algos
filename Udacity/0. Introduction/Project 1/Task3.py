"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv, re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Declare variables
PRINT_MSG_3 = """The numbers called by people in Bangalore have codes:"""
PRINT_MSG_FORMATTER = 52
area_codes = {} # dict()
bangalore_calls = [call for call in calls if call[0].startswith('(080)')]


def print_task3(area_codes, fixed_lines, all_lines, print_msg, formatter=52):
    # print('-' * formatter + 'Task 3' + '-' * formatter)
    # print('Part A:')
    print(print_msg)
    for i in sorted(area_codes): print(i)
    # print(); print()
    # print('Part B:')
    print(f'{round(fixed_lines/all_lines*100, 2)}% percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')


for call in bangalore_calls:
    # Fixed Lines start with an area code enclosed in brackets.
    # The area codes vary in length but always begin with 0.

    if call[1].startswith('(') and call[1][1] == '0':
        if re.match(r"\(([0-9]+)\)", call[1]).group(0)[1:-1] in area_codes:
            area_codes[re.match(r"\(([0-9]+)\)", call[1]).group(0)[1:-1]] += 1
        else:
            area_codes[re.match(r"\(([0-9]+)\)", call[1]).group(0)[1:-1]] = 1

    # Mobile Lines have no parentheses, but have a space in the middle of the number to help readability.
    # The prefix is its first four digits, and they always start with 7, 8, 9

    elif call[1].startswith(('7', '8', '9')):
        if call[1].split(' ')[0][:4] in area_codes:
            area_codes[call[1].split(' ')[0][:4]] += 1
        else:
            area_codes[call[1].split(' ')[0][:4]] = 1

    # telemarketers
    elif call[1].startswith(r'140'):
        if call[1][:3] in area_codes:
            area_codes[call[1][:3]] += 1
        else:
            area_codes[call[1][:3]] = 1


if __name__ == '__main__':
    fixedlines = area_codes['080']
    alllines = len(bangalore_calls)
    print_task3(area_codes, fixedlines, alllines, PRINT_MSG_3)
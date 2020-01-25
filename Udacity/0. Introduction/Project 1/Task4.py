"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Declare variables
PRINT_MSG_4 = """These numbers could be telemarketers: """
incoming_calls, incoming_texts, outgoing_calls, outgoing_texts = set(), set(), set(), set()


def print_task4(print_msg, list_of_numbers, formatter=52):
    print(print_msg)
    for i in list_of_numbers: print(i)


for call in calls:
    outgoing_calls.add(call[0])
    incoming_calls.add(call[1])

for text in texts:
    outgoing_texts.add(text[0])
    incoming_texts.add(text[1])


if __name__ == '__main__':
    # final_set = {element for element in incoming_calls if element not in outgoing_calls and element not in outgoing_texts and element not in incoming_texts}
    final_list = list(sorted(outgoing_calls - (incoming_calls | incoming_texts | outgoing_texts)))  # set difference = outgoing_calls - incoming_calls - incoming_texts - outgoing_texts
    print_task4(PRINT_MSG_4, final_list)
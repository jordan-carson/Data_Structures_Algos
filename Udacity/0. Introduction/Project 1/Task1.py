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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def print_task1(unique_set, formatter=52):
    print(f'There are {len(unique_set)} different telephone numbers in the records.')

# Declare variables
unique_phone_numbers = set()

for call in calls:
    unique_phone_numbers.add(call[0])
    unique_phone_numbers.add(call[1])

for text in texts:
    unique_phone_numbers.add(text[0])
    unique_phone_numbers.add(text[1])


if __name__ == '__main__':
    print_task1(unique_phone_numbers)

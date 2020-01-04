"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Declare variables
time_dictionary = dict()


# Create printing task
def prnt_task2(time_dict, longest_phone_number, formatter=52):
    print(f'{longest_phone_number} spent the longest time, {time_dict[longest_phone_number]} seconds, on the phone during September 2016.')


for call in calls:
    if call[0] in time_dictionary:
        time_dictionary[call[0]] += int(call[3])
    else:
        time_dictionary[call[0]] = int(call[3])

    if call[1] in time_dictionary:
        time_dictionary[call[1]] += int(call[3])
    else:
        time_dictionary[call[1]] = int(call[3])


if __name__ == '__main__':
    longest_phone = sorted(time_dictionary, key=time_dictionary.get, reverse=True)[0]
    prnt_task2(time_dictionary, longest_phone)
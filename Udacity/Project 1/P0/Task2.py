"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import OrderedDict
import sys

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

longest = 0
time_d = dict()
phone_temp = ""

for call in calls:
    if call[0] in time_d:
        time_d[call[0]] += int(call[3])
    else:
        time_d[call[0]] = int(call[3])

    if call[1] in time_d:
        time_d[call[1]] += int(call[3])
    else:
        time_d[call[1]] = int(call[3])

if '3.7' in sys.version:
    final = OrderedDict({k: v for k, v in sorted(time_d.items(), key=lambda item: item[1])})
    final_items = list(final.popitem())
    print(f"{final_items[0]} spent the longest time, {final_items[1]} seconds, on the phone during September 2016.")
else:
    final = sorted(time_d, key=time_d.get, reverse=True)[0]
    print('{0} spent the longest time, {1} seconds, on the phone during September 2016'.format(final, time_d[final]))

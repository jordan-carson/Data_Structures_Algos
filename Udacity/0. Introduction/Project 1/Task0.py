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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def print_task0(t, c):
    print(f"First record of texts, {t[0][0]} texts {t[0][1]} at time {t[0][2]}.")
    print(f"Last record of calls, {c[-1][0]} calls {c[-1][1]} at time {c[-1][2]}, lasting {c[-1][3]} seconds.")


if __name__ == '__main__':
    print_task0(texts, calls)


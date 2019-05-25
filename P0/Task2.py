"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

from Task1 import tel_numbers

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
number_durations = { number: 0 for number in tel_numbers() }

for number in number_durations.keys():
    for index, call in enumerate(calls):
        if number == call[0] or number == call[1]:
            number_durations[number] += int(call[3])


longest_call_duration = max(number_durations.values())
longest_call_duration_by = list(number_durations.keys())[list(number_durations.values()).index(longest_call_duration)]

print(f"{longest_call_duration_by!r} spent the longest time, {longest_call_duration!r} seconds, on the phone during September 2016.")

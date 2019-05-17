"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

from Task2 import callers, recipients

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
texters = []
text_recipients = []
for text in texts:
    texters.append(text[0])
    text_recipients.append(text[1])

telemarketers = []
others = []
for caller in callers:
    if caller not in recipients and caller not in texters and caller not in text_recipients:
        telemarketers.append(caller)
        
telemarketers = list(set(telemarketers))
telemarketers.sort()

print("These numbers could be telemarketers: ")
print(*telemarketers, sep="\n")
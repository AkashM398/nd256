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
"""
codes_and_prefixes_called_from_bangalore = []
for caller_index, number in enumerate(callers):
  if number.startswith("(080)"):
    recipient = recipients[caller_index]
    if recipient.startswith("(0"):
      area_code = recipient.split(")")[0][1:]
      codes_and_prefixes_called_from_bangalore.append(area_code)
    elif " " in recipient:
      prefix = recipient[:4]
      codes_and_prefixes_called_from_bangalore.append(prefix)

codes_and_prefixes = list(set(codes_and_prefixes_called_from_bangalore))
codes_and_prefixes.sort()
print("The numbers called by people in Bangalore have codes:")
print(*codes_and_prefixes, sep="\n")
"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
percentage_calls = (codes_and_prefixes_called_from_bangalore.count("080") / len(codes_and_prefixes_called_from_bangalore)) * 100
print(f"\n{percentage_calls:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
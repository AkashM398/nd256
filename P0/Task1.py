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
def tel_numbers():
    """Returns set of all telephone numbers in texts and calls
    """
    all_numbers = set()
    for number in (texts + calls):
        all_numbers.add(number[0])
        all_numbers.add(number[1])
    
    return all_numbers

print(f"There are {len(tel_numbers())} different telephone numbers in the records.")
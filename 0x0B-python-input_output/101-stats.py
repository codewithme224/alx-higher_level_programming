#!/usr/bin/python3
"""Module for stdin metrics"""


import sys
import signal

# Define a dictionary to store the file size and status code counts
file_sizes = []
status_counts = {}

# Define a signal handler to catch keyboard interrupts
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Define a function to print the statistics
def print_statistics():
    total_size = sum(file_sizes)
    print(f'Total file size: {total_size}')
    for code in sorted(status_counts.keys()):
        print(f'{code}: {status_counts[code]}')

# Register the signal handler for keyboard interrupts
signal.signal(signal.SIGINT, signal_handler)

# Read input from stdin line by line
for line_number, line in enumerate(sys.stdin, start=1):
    # Parse the input line
    ip, _, _, status_code, file_size = line.split()

    # Update the file size count
    file_sizes.append(int(file_size))

    # Update the status code count
    if status_code in status_counts:
        status_counts[status_code] += 1
    else:
        status_counts[status_code] = 1

    # Print the statistics every 10 lines
    if line_number % 10 == 0:
        print_statistics()

# Print the final statistics
print_statistics()


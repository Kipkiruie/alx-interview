The 0x03-log_parsing project is a programming exercise aimed at teaching and testing skills in real-time data stream processing using Python. The project involves reading log data from standard input, parsing the data to extract specific information, and performing calculations based on the parsed data. The goal is to track and report on specific metrics derived from the log data.

Key Concepts
File I/O in Python:

Reading from standard input (stdin) line by line.
Understanding Python's input and output operations.
Signal Handling in Python:

Handling keyboard interruptions (CTRL + C) using signal handling to ensure graceful shutdown and final reporting.
Data Processing:

Parsing strings to extract specific data points.
Aggregating data to compute summaries and metrics.
Regular Expressions:

Using regular expressions to validate and parse each line of log data.
Dictionaries in Python:

Using dictionaries to count occurrences of status codes and accumulate file sizes.
Exception Handling:

Handling possible exceptions during file reading and data processing to ensure robustness.
Task Requirements
Input Format:
The log entries have a specific format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Lines that do not match this format should be skipped.

Output Metrics:

Total file size: The sum of all file sizes from the logs.
Number of lines by status code: The count of occurrences of each status code (200, 301, 400, 401, 403, 404, 405, 500).
Output Conditions:

Metrics should be printed every 10 lines and upon receiving a keyboard interruption (CTRL + C).
Status codes should be printed in ascending order.
Example
Here's an example of how the script should behave. Given a log generator script 0-generator.py that generates log entries, the log parsing script 0-stats.py should read these entries from stdin and print the metrics as described.

Log Entry Example:

yaml
Copy code
127.0.0.1 - [2022-03-22 10:00:00.000] "GET /projects/260 HTTP/1.1" 200 1024
Script Execution Example:

bash
Copy code
./0-generator.py | ./0-stats.py
Expected Output Example:

yaml
Copy code
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
...
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Implementation
Here is a complete Python script for the 0-stats.py file to handle the log parsing requirements:

python
Copy code
#!/usr/bin/python3
import sys
import signal
import re

# Initialize variables
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_statistics():
    """Print the accumulated metrics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle the keyboard interrupt signal."""
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Regular expression to match the log line format
log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total_file_size += file_size
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)

print_statistics()
Running the Script
To execute the script, make sure it is executable:

bash
Copy code
chmod +x 0-stats.py
Then, you can run it with the log generator:

bash
Copy code
./0-generator.py | ./0-stats.py
This will read the generated log entries, parse them, and print the required metrics every 10 lines or upon receiving a keyboard interrupt (CTRL + C).

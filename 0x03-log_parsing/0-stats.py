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

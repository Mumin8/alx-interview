#!/usr/bin/python3
'''0-stats'''

import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) != 7:
            continue

        ip, date, _, status_code, file_size = parts[:5]
        if status_code.isdigit():
            status_counts[status_code] += 1
            total_size += int(file_size)

        line_count += 1

        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

#!/usr/bin/python3
'''0-stats'''

import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            ip, _, _, status, size = line.split()[0], line.split()[5], line.split()[
                6], int(line.split()[8]), int(line.split()[9])
        except ValueError:
            continue

        total_size += size
        status_codes[status] = status_codes.get(status, 0) + 1
        line_count += 1

        if line_count % 10 == 0:
            print(f"Total file size: {total_size}")
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}: {status_codes[code]}")

except KeyboardInterrupt:
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

#!/usr/bin/python3
'''0-validate_utf8'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    num_expected_bytes = 0
    for byte in data:
        if num_expected_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_expected_bytes = 1
            elif byte >> 4 == 0b1110:
                num_expected_bytes = 2
            elif byte >> 3 == 0b11110:
                num_expected_bytes = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_expected_bytes -= 1

    return num_expected_bytes == 0

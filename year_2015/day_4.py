import hashlib
import sys


def compute_hash(input, zeros_count):
    input = input.strip()

    for i in range(1, sys.maxsize):
        s = f'{input}{i}'

        if hashlib.md5(s.encode()).hexdigest().startswith('0' * zeros_count):
            return i

    return ''


def level_1(input):
    return compute_hash(input, 5)


def level_2(input):
    return compute_hash(input, 6)
